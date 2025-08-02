_M='l2tpSessionLocalSessionId'
_L='shutdown'
_K='established'
_J='l2tpTunnelLocalTunnelId'
_I='l2tpTunnelProfileIndex'
_H='enabled'
_G='disabled'
_F='BIANCA-BRICK-L2TP-MIB'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Vpn_ObjectIdentity=ObjectIdentity
vpn=_Vpn_ObjectIdentity((1,3,6,1,4,1,272,4,23))
_L2tp_ObjectIdentity=ObjectIdentity
l2tp=_L2tp_ObjectIdentity((1,3,6,1,4,1,272,4,23,8))
_L2tpGlobals_ObjectIdentity=ObjectIdentity
l2tpGlobals=_L2tpGlobals_ObjectIdentity((1,3,6,1,4,1,272,4,23,8,10))
class _L2tpGlobUdpPort_Type(Integer32):defaultValue=1701;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_L2tpGlobUdpPort_Type.__name__=_B
_L2tpGlobUdpPort_Object=MibScalar
l2tpGlobUdpPort=_L2tpGlobUdpPort_Object((1,3,6,1,4,1,272,4,23,8,10,10),_L2tpGlobUdpPort_Type())
l2tpGlobUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpGlobUdpPort.setStatus(_A)
class _L2tpGlobPortUsage_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('single',1),('floating',2)))
_L2tpGlobPortUsage_Type.__name__=_B
_L2tpGlobPortUsage_Object=MibScalar
l2tpGlobPortUsage=_L2tpGlobPortUsage_Object((1,3,6,1,4,1,272,4,23,8,10,20),_L2tpGlobPortUsage_Type())
l2tpGlobPortUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpGlobPortUsage.setStatus(_A)
_L2tpTunnelProfileTable_Object=MibTable
l2tpTunnelProfileTable=_L2tpTunnelProfileTable_Object((1,3,6,1,4,1,272,4,23,8,20))
if mibBuilder.loadTexts:l2tpTunnelProfileTable.setStatus(_A)
_L2tpTunnelProfileEntry_Object=MibTableRow
l2tpTunnelProfileEntry=_L2tpTunnelProfileEntry_Object((1,3,6,1,4,1,272,4,23,8,20,10))
l2tpTunnelProfileEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:l2tpTunnelProfileEntry.setStatus(_A)
class _L2tpTunnelProfileIndex_Type(Integer32):defaultValue=0
_L2tpTunnelProfileIndex_Type.__name__=_B
_L2tpTunnelProfileIndex_Object=MibTableColumn
l2tpTunnelProfileIndex=_L2tpTunnelProfileIndex_Object((1,3,6,1,4,1,272,4,23,8,20,10,10),_L2tpTunnelProfileIndex_Type())
l2tpTunnelProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileIndex.setStatus(_A)
class _L2tpTunnelProfileName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelProfileName_Type.__name__=_E
_L2tpTunnelProfileName_Object=MibTableColumn
l2tpTunnelProfileName=_L2tpTunnelProfileName_Object((1,3,6,1,4,1,272,4,23,8,20,10,15),_L2tpTunnelProfileName_Type())
l2tpTunnelProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileName.setStatus(_A)
_L2tpTunnelProfileRemoteIpAddress_Type=IpAddress
_L2tpTunnelProfileRemoteIpAddress_Object=MibTableColumn
l2tpTunnelProfileRemoteIpAddress=_L2tpTunnelProfileRemoteIpAddress_Object((1,3,6,1,4,1,272,4,23,8,20,10,20),_L2tpTunnelProfileRemoteIpAddress_Type())
l2tpTunnelProfileRemoteIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileRemoteIpAddress.setStatus(_A)
_L2tpTunnelProfileRemoteIpAddressBackup_Type=IpAddress
_L2tpTunnelProfileRemoteIpAddressBackup_Object=MibTableColumn
l2tpTunnelProfileRemoteIpAddressBackup=_L2tpTunnelProfileRemoteIpAddressBackup_Object((1,3,6,1,4,1,272,4,23,8,20,10,25),_L2tpTunnelProfileRemoteIpAddressBackup_Type())
l2tpTunnelProfileRemoteIpAddressBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileRemoteIpAddressBackup.setStatus(_A)
class _L2tpTunnelProfileRemoteUdpPort_Type(Integer32):defaultValue=1701;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpTunnelProfileRemoteUdpPort_Type.__name__=_B
_L2tpTunnelProfileRemoteUdpPort_Object=MibTableColumn
l2tpTunnelProfileRemoteUdpPort=_L2tpTunnelProfileRemoteUdpPort_Object((1,3,6,1,4,1,272,4,23,8,20,10,30),_L2tpTunnelProfileRemoteUdpPort_Type())
l2tpTunnelProfileRemoteUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileRemoteUdpPort.setStatus(_A)
class _L2tpTunnelProfileRemoteHostname_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelProfileRemoteHostname_Type.__name__=_E
_L2tpTunnelProfileRemoteHostname_Object=MibTableColumn
l2tpTunnelProfileRemoteHostname=_L2tpTunnelProfileRemoteHostname_Object((1,3,6,1,4,1,272,4,23,8,20,10,40),_L2tpTunnelProfileRemoteHostname_Type())
l2tpTunnelProfileRemoteHostname.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileRemoteHostname.setStatus(_A)
_L2tpTunnelProfileLocalIpAddress_Type=IpAddress
_L2tpTunnelProfileLocalIpAddress_Object=MibTableColumn
l2tpTunnelProfileLocalIpAddress=_L2tpTunnelProfileLocalIpAddress_Object((1,3,6,1,4,1,272,4,23,8,20,10,50),_L2tpTunnelProfileLocalIpAddress_Type())
l2tpTunnelProfileLocalIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileLocalIpAddress.setStatus(_A)
class _L2tpTunnelProfileLocalUdpPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpTunnelProfileLocalUdpPort_Type.__name__=_B
_L2tpTunnelProfileLocalUdpPort_Object=MibTableColumn
l2tpTunnelProfileLocalUdpPort=_L2tpTunnelProfileLocalUdpPort_Object((1,3,6,1,4,1,272,4,23,8,20,10,60),_L2tpTunnelProfileLocalUdpPort_Type())
l2tpTunnelProfileLocalUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileLocalUdpPort.setStatus(_A)
class _L2tpTunnelProfileLocalHostname_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelProfileLocalHostname_Type.__name__=_E
_L2tpTunnelProfileLocalHostname_Object=MibTableColumn
l2tpTunnelProfileLocalHostname=_L2tpTunnelProfileLocalHostname_Object((1,3,6,1,4,1,272,4,23,8,20,10,70),_L2tpTunnelProfileLocalHostname_Type())
l2tpTunnelProfileLocalHostname.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileLocalHostname.setStatus(_A)
class _L2tpTunnelProfilePassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelProfilePassword_Type.__name__=_E
_L2tpTunnelProfilePassword_Object=MibTableColumn
l2tpTunnelProfilePassword=_L2tpTunnelProfilePassword_Object((1,3,6,1,4,1,272,4,23,8,20,10,80),_L2tpTunnelProfilePassword_Type())
l2tpTunnelProfilePassword.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfilePassword.setStatus(_A)
class _L2tpTunnelProfileReceiveWindowSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_L2tpTunnelProfileReceiveWindowSize_Type.__name__=_B
_L2tpTunnelProfileReceiveWindowSize_Object=MibTableColumn
l2tpTunnelProfileReceiveWindowSize=_L2tpTunnelProfileReceiveWindowSize_Object((1,3,6,1,4,1,272,4,23,8,20,10,90),_L2tpTunnelProfileReceiveWindowSize_Type())
l2tpTunnelProfileReceiveWindowSize.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileReceiveWindowSize.setStatus(_A)
class _L2tpTunnelProfileHelloInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_L2tpTunnelProfileHelloInterval_Type.__name__=_B
_L2tpTunnelProfileHelloInterval_Object=MibTableColumn
l2tpTunnelProfileHelloInterval=_L2tpTunnelProfileHelloInterval_Object((1,3,6,1,4,1,272,4,23,8,20,10,100),_L2tpTunnelProfileHelloInterval_Type())
l2tpTunnelProfileHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileHelloInterval.setStatus(_A)
class _L2tpTunnelProfileSessionDataSequencing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('delete',1),(_G,2),(_H,3)))
_L2tpTunnelProfileSessionDataSequencing_Type.__name__=_B
_L2tpTunnelProfileSessionDataSequencing_Object=MibTableColumn
l2tpTunnelProfileSessionDataSequencing=_L2tpTunnelProfileSessionDataSequencing_Object((1,3,6,1,4,1,272,4,23,8,20,10,110),_L2tpTunnelProfileSessionDataSequencing_Type())
l2tpTunnelProfileSessionDataSequencing.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileSessionDataSequencing.setStatus(_A)
class _L2tpTunnelProfileMinRetryTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_L2tpTunnelProfileMinRetryTime_Type.__name__=_B
_L2tpTunnelProfileMinRetryTime_Object=MibTableColumn
l2tpTunnelProfileMinRetryTime=_L2tpTunnelProfileMinRetryTime_Object((1,3,6,1,4,1,272,4,23,8,20,10,120),_L2tpTunnelProfileMinRetryTime_Type())
l2tpTunnelProfileMinRetryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileMinRetryTime.setStatus(_A)
class _L2tpTunnelProfileMaxRetryTime_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,255))
_L2tpTunnelProfileMaxRetryTime_Type.__name__=_B
_L2tpTunnelProfileMaxRetryTime_Object=MibTableColumn
l2tpTunnelProfileMaxRetryTime=_L2tpTunnelProfileMaxRetryTime_Object((1,3,6,1,4,1,272,4,23,8,20,10,130),_L2tpTunnelProfileMaxRetryTime_Type())
l2tpTunnelProfileMaxRetryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileMaxRetryTime.setStatus(_A)
class _L2tpTunnelProfileMaxRetries_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_L2tpTunnelProfileMaxRetries_Type.__name__=_B
_L2tpTunnelProfileMaxRetries_Object=MibTableColumn
l2tpTunnelProfileMaxRetries=_L2tpTunnelProfileMaxRetries_Object((1,3,6,1,4,1,272,4,23,8,20,10,140),_L2tpTunnelProfileMaxRetries_Type())
l2tpTunnelProfileMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileMaxRetries.setStatus(_A)
class _L2tpTunnelProfileRadiusAssignment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_L2tpTunnelProfileRadiusAssignment_Type.__name__=_B
_L2tpTunnelProfileRadiusAssignment_Object=MibTableColumn
l2tpTunnelProfileRadiusAssignment=_L2tpTunnelProfileRadiusAssignment_Object((1,3,6,1,4,1,272,4,23,8,20,10,150),_L2tpTunnelProfileRadiusAssignment_Type())
l2tpTunnelProfileRadiusAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileRadiusAssignment.setStatus(_A)
class _L2tpTunnelProfileRadiusGroupId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_L2tpTunnelProfileRadiusGroupId_Type.__name__=_B
_L2tpTunnelProfileRadiusGroupId_Object=MibTableColumn
l2tpTunnelProfileRadiusGroupId=_L2tpTunnelProfileRadiusGroupId_Object((1,3,6,1,4,1,272,4,23,8,20,10,160),_L2tpTunnelProfileRadiusGroupId_Type())
l2tpTunnelProfileRadiusGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelProfileRadiusGroupId.setStatus(_A)
_L2tpTunnelTable_Object=MibTable
l2tpTunnelTable=_L2tpTunnelTable_Object((1,3,6,1,4,1,272,4,23,8,30))
if mibBuilder.loadTexts:l2tpTunnelTable.setStatus(_A)
_L2tpTunnelEntry_Object=MibTableRow
l2tpTunnelEntry=_L2tpTunnelEntry_Object((1,3,6,1,4,1,272,4,23,8,30,10))
l2tpTunnelEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:l2tpTunnelEntry.setStatus(_A)
_L2tpTunnelRemoteIpAddress_Type=IpAddress
_L2tpTunnelRemoteIpAddress_Object=MibTableColumn
l2tpTunnelRemoteIpAddress=_L2tpTunnelRemoteIpAddress_Object((1,3,6,1,4,1,272,4,23,8,30,10,10),_L2tpTunnelRemoteIpAddress_Type())
l2tpTunnelRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelRemoteIpAddress.setStatus(_A)
class _L2tpTunnelRemoteUdpPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpTunnelRemoteUdpPort_Type.__name__=_B
_L2tpTunnelRemoteUdpPort_Object=MibTableColumn
l2tpTunnelRemoteUdpPort=_L2tpTunnelRemoteUdpPort_Object((1,3,6,1,4,1,272,4,23,8,30,10,20),_L2tpTunnelRemoteUdpPort_Type())
l2tpTunnelRemoteUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelRemoteUdpPort.setStatus(_A)
class _L2tpTunnelRemoteTunnelId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpTunnelRemoteTunnelId_Type.__name__=_B
_L2tpTunnelRemoteTunnelId_Object=MibTableColumn
l2tpTunnelRemoteTunnelId=_L2tpTunnelRemoteTunnelId_Object((1,3,6,1,4,1,272,4,23,8,30,10,30),_L2tpTunnelRemoteTunnelId_Type())
l2tpTunnelRemoteTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelRemoteTunnelId.setStatus(_A)
class _L2tpTunnelRemoteReceiveWindowSize_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_L2tpTunnelRemoteReceiveWindowSize_Type.__name__=_B
_L2tpTunnelRemoteReceiveWindowSize_Object=MibTableColumn
l2tpTunnelRemoteReceiveWindowSize=_L2tpTunnelRemoteReceiveWindowSize_Object((1,3,6,1,4,1,272,4,23,8,30,10,35),_L2tpTunnelRemoteReceiveWindowSize_Type())
l2tpTunnelRemoteReceiveWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelRemoteReceiveWindowSize.setStatus(_A)
class _L2tpTunnelRemoteHostname_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelRemoteHostname_Type.__name__=_E
_L2tpTunnelRemoteHostname_Object=MibTableColumn
l2tpTunnelRemoteHostname=_L2tpTunnelRemoteHostname_Object((1,3,6,1,4,1,272,4,23,8,30,10,40),_L2tpTunnelRemoteHostname_Type())
l2tpTunnelRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelRemoteHostname.setStatus(_A)
class _L2tpTunnelRemoteVendorName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelRemoteVendorName_Type.__name__=_E
_L2tpTunnelRemoteVendorName_Object=MibTableColumn
l2tpTunnelRemoteVendorName=_L2tpTunnelRemoteVendorName_Object((1,3,6,1,4,1,272,4,23,8,30,10,50),_L2tpTunnelRemoteVendorName_Type())
l2tpTunnelRemoteVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelRemoteVendorName.setStatus(_A)
_L2tpTunnelLocalIpAddress_Type=IpAddress
_L2tpTunnelLocalIpAddress_Object=MibTableColumn
l2tpTunnelLocalIpAddress=_L2tpTunnelLocalIpAddress_Object((1,3,6,1,4,1,272,4,23,8,30,10,60),_L2tpTunnelLocalIpAddress_Type())
l2tpTunnelLocalIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelLocalIpAddress.setStatus(_A)
class _L2tpTunnelLocalUdpPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpTunnelLocalUdpPort_Type.__name__=_B
_L2tpTunnelLocalUdpPort_Object=MibTableColumn
l2tpTunnelLocalUdpPort=_L2tpTunnelLocalUdpPort_Object((1,3,6,1,4,1,272,4,23,8,30,10,70),_L2tpTunnelLocalUdpPort_Type())
l2tpTunnelLocalUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelLocalUdpPort.setStatus(_A)
class _L2tpTunnelLocalTunnelId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpTunnelLocalTunnelId_Type.__name__=_B
_L2tpTunnelLocalTunnelId_Object=MibTableColumn
l2tpTunnelLocalTunnelId=_L2tpTunnelLocalTunnelId_Object((1,3,6,1,4,1,272,4,23,8,30,10,80),_L2tpTunnelLocalTunnelId_Type())
l2tpTunnelLocalTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelLocalTunnelId.setStatus(_A)
class _L2tpTunnelLocalReceiveWindowSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_L2tpTunnelLocalReceiveWindowSize_Type.__name__=_B
_L2tpTunnelLocalReceiveWindowSize_Object=MibTableColumn
l2tpTunnelLocalReceiveWindowSize=_L2tpTunnelLocalReceiveWindowSize_Object((1,3,6,1,4,1,272,4,23,8,30,10,85),_L2tpTunnelLocalReceiveWindowSize_Type())
l2tpTunnelLocalReceiveWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelLocalReceiveWindowSize.setStatus(_A)
class _L2tpTunnelLocalHostname_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelLocalHostname_Type.__name__=_E
_L2tpTunnelLocalHostname_Object=MibTableColumn
l2tpTunnelLocalHostname=_L2tpTunnelLocalHostname_Object((1,3,6,1,4,1,272,4,23,8,30,10,90),_L2tpTunnelLocalHostname_Type())
l2tpTunnelLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelLocalHostname.setStatus(_A)
class _L2tpTunnelPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpTunnelPassword_Type.__name__=_E
_L2tpTunnelPassword_Object=MibTableColumn
l2tpTunnelPassword=_L2tpTunnelPassword_Object((1,3,6,1,4,1,272,4,23,8,30,10,100),_L2tpTunnelPassword_Type())
l2tpTunnelPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpTunnelPassword.setStatus(_A)
class _L2tpTunnelHelloInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_L2tpTunnelHelloInterval_Type.__name__=_B
_L2tpTunnelHelloInterval_Object=MibTableColumn
l2tpTunnelHelloInterval=_L2tpTunnelHelloInterval_Object((1,3,6,1,4,1,272,4,23,8,30,10,120),_L2tpTunnelHelloInterval_Type())
l2tpTunnelHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelHelloInterval.setStatus(_A)
class _L2tpTunnelSessionDataSequencing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_L2tpTunnelSessionDataSequencing_Type.__name__=_B
_L2tpTunnelSessionDataSequencing_Object=MibTableColumn
l2tpTunnelSessionDataSequencing=_L2tpTunnelSessionDataSequencing_Object((1,3,6,1,4,1,272,4,23,8,30,10,130),_L2tpTunnelSessionDataSequencing_Type())
l2tpTunnelSessionDataSequencing.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelSessionDataSequencing.setStatus(_A)
class _L2tpTunnelMinRetryTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_L2tpTunnelMinRetryTime_Type.__name__=_B
_L2tpTunnelMinRetryTime_Object=MibTableColumn
l2tpTunnelMinRetryTime=_L2tpTunnelMinRetryTime_Object((1,3,6,1,4,1,272,4,23,8,30,10,140),_L2tpTunnelMinRetryTime_Type())
l2tpTunnelMinRetryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelMinRetryTime.setStatus(_A)
class _L2tpTunnelMaxRetryTime_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,255))
_L2tpTunnelMaxRetryTime_Type.__name__=_B
_L2tpTunnelMaxRetryTime_Object=MibTableColumn
l2tpTunnelMaxRetryTime=_L2tpTunnelMaxRetryTime_Object((1,3,6,1,4,1,272,4,23,8,30,10,150),_L2tpTunnelMaxRetryTime_Type())
l2tpTunnelMaxRetryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelMaxRetryTime.setStatus(_A)
class _L2tpTunnelMaxRetries_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_L2tpTunnelMaxRetries_Type.__name__=_B
_L2tpTunnelMaxRetries_Object=MibTableColumn
l2tpTunnelMaxRetries=_L2tpTunnelMaxRetries_Object((1,3,6,1,4,1,272,4,23,8,30,10,160),_L2tpTunnelMaxRetries_Type())
l2tpTunnelMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelMaxRetries.setStatus(_A)
class _L2tpTunnelState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('waitctlreply',2),('waitctlconn',3),(_K,4),(_L,5)))
_L2tpTunnelState_Type.__name__=_B
_L2tpTunnelState_Object=MibTableColumn
l2tpTunnelState=_L2tpTunnelState_Object((1,3,6,1,4,1,272,4,23,8,30,10,170),_L2tpTunnelState_Type())
l2tpTunnelState.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpTunnelState.setStatus(_A)
_L2tpSessionTable_Object=MibTable
l2tpSessionTable=_L2tpSessionTable_Object((1,3,6,1,4,1,272,4,23,8,40))
if mibBuilder.loadTexts:l2tpSessionTable.setStatus(_A)
_L2tpSessionEntry_Object=MibTableRow
l2tpSessionEntry=_L2tpSessionEntry_Object((1,3,6,1,4,1,272,4,23,8,40,10))
l2tpSessionEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:l2tpSessionEntry.setStatus(_A)
_L2tpSessionRemoteIpAddress_Type=IpAddress
_L2tpSessionRemoteIpAddress_Object=MibTableColumn
l2tpSessionRemoteIpAddress=_L2tpSessionRemoteIpAddress_Object((1,3,6,1,4,1,272,4,23,8,40,10,10),_L2tpSessionRemoteIpAddress_Type())
l2tpSessionRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionRemoteIpAddress.setStatus(_A)
class _L2tpSessionRemoteUdpPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpSessionRemoteUdpPort_Type.__name__=_B
_L2tpSessionRemoteUdpPort_Object=MibTableColumn
l2tpSessionRemoteUdpPort=_L2tpSessionRemoteUdpPort_Object((1,3,6,1,4,1,272,4,23,8,40,10,20),_L2tpSessionRemoteUdpPort_Type())
l2tpSessionRemoteUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionRemoteUdpPort.setStatus(_A)
class _L2tpSessionRemoteTunnelId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpSessionRemoteTunnelId_Type.__name__=_B
_L2tpSessionRemoteTunnelId_Object=MibTableColumn
l2tpSessionRemoteTunnelId=_L2tpSessionRemoteTunnelId_Object((1,3,6,1,4,1,272,4,23,8,40,10,30),_L2tpSessionRemoteTunnelId_Type())
l2tpSessionRemoteTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionRemoteTunnelId.setStatus(_A)
class _L2tpSessionRemoteSessionId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpSessionRemoteSessionId_Type.__name__=_B
_L2tpSessionRemoteSessionId_Object=MibTableColumn
l2tpSessionRemoteSessionId=_L2tpSessionRemoteSessionId_Object((1,3,6,1,4,1,272,4,23,8,40,10,40),_L2tpSessionRemoteSessionId_Type())
l2tpSessionRemoteSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionRemoteSessionId.setStatus(_A)
class _L2tpSessionRemoteHostname_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpSessionRemoteHostname_Type.__name__=_E
_L2tpSessionRemoteHostname_Object=MibTableColumn
l2tpSessionRemoteHostname=_L2tpSessionRemoteHostname_Object((1,3,6,1,4,1,272,4,23,8,40,10,50),_L2tpSessionRemoteHostname_Type())
l2tpSessionRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionRemoteHostname.setStatus(_A)
_L2tpSessionLocalIpAddress_Type=IpAddress
_L2tpSessionLocalIpAddress_Object=MibTableColumn
l2tpSessionLocalIpAddress=_L2tpSessionLocalIpAddress_Object((1,3,6,1,4,1,272,4,23,8,40,10,60),_L2tpSessionLocalIpAddress_Type())
l2tpSessionLocalIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionLocalIpAddress.setStatus(_A)
class _L2tpSessionLocalUdpPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpSessionLocalUdpPort_Type.__name__=_B
_L2tpSessionLocalUdpPort_Object=MibTableColumn
l2tpSessionLocalUdpPort=_L2tpSessionLocalUdpPort_Object((1,3,6,1,4,1,272,4,23,8,40,10,70),_L2tpSessionLocalUdpPort_Type())
l2tpSessionLocalUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionLocalUdpPort.setStatus(_A)
class _L2tpSessionLocalTunnelId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpSessionLocalTunnelId_Type.__name__=_B
_L2tpSessionLocalTunnelId_Object=MibTableColumn
l2tpSessionLocalTunnelId=_L2tpSessionLocalTunnelId_Object((1,3,6,1,4,1,272,4,23,8,40,10,80),_L2tpSessionLocalTunnelId_Type())
l2tpSessionLocalTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionLocalTunnelId.setStatus(_A)
class _L2tpSessionLocalSessionId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpSessionLocalSessionId_Type.__name__=_B
_L2tpSessionLocalSessionId_Object=MibTableColumn
l2tpSessionLocalSessionId=_L2tpSessionLocalSessionId_Object((1,3,6,1,4,1,272,4,23,8,40,10,90),_L2tpSessionLocalSessionId_Type())
l2tpSessionLocalSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionLocalSessionId.setStatus(_A)
class _L2tpSessionLocalHostname_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpSessionLocalHostname_Type.__name__=_E
_L2tpSessionLocalHostname_Object=MibTableColumn
l2tpSessionLocalHostname=_L2tpSessionLocalHostname_Object((1,3,6,1,4,1,272,4,23,8,40,10,100),_L2tpSessionLocalHostname_Type())
l2tpSessionLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionLocalHostname.setStatus(_A)
class _L2tpSessionCallSerialNumber_Type(Integer32):defaultValue=0
_L2tpSessionCallSerialNumber_Type.__name__=_B
_L2tpSessionCallSerialNumber_Object=MibTableColumn
l2tpSessionCallSerialNumber=_L2tpSessionCallSerialNumber_Object((1,3,6,1,4,1,272,4,23,8,40,10,110),_L2tpSessionCallSerialNumber_Type())
l2tpSessionCallSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionCallSerialNumber.setStatus(_A)
class _L2tpSessionDataSequencing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_L2tpSessionDataSequencing_Type.__name__=_B
_L2tpSessionDataSequencing_Object=MibTableColumn
l2tpSessionDataSequencing=_L2tpSessionDataSequencing_Object((1,3,6,1,4,1,272,4,23,8,40,10,120),_L2tpSessionDataSequencing_Type())
l2tpSessionDataSequencing.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpSessionDataSequencing.setStatus(_A)
class _L2tpSessionState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('idle',1),('waittunnel',2),('waitcsanswer',3),('waitreply',4),('waitconnect',5),(_K,6),(_L,7)))
_L2tpSessionState_Type.__name__=_B
_L2tpSessionState_Object=MibTableColumn
l2tpSessionState=_L2tpSessionState_Object((1,3,6,1,4,1,272,4,23,8,40,10,130),_L2tpSessionState_Type())
l2tpSessionState.setMaxAccess(_D)
if mibBuilder.loadTexts:l2tpSessionState.setStatus(_A)
class _L2tpSessionInfo_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_L2tpSessionInfo_Type.__name__=_E
_L2tpSessionInfo_Object=MibTableColumn
l2tpSessionInfo=_L2tpSessionInfo_Object((1,3,6,1,4,1,272,4,23,8,40,10,140),_L2tpSessionInfo_Type())
l2tpSessionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionInfo.setStatus(_A)
class _L2tpSessionClientPPPCrcErrors_Type(Integer32):defaultValue=0
_L2tpSessionClientPPPCrcErrors_Type.__name__=_B
_L2tpSessionClientPPPCrcErrors_Object=MibTableColumn
l2tpSessionClientPPPCrcErrors=_L2tpSessionClientPPPCrcErrors_Object((1,3,6,1,4,1,272,4,23,8,40,10,150),_L2tpSessionClientPPPCrcErrors_Type())
l2tpSessionClientPPPCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionClientPPPCrcErrors.setStatus(_A)
class _L2tpSessionClientPPPFramingErrors_Type(Integer32):defaultValue=0
_L2tpSessionClientPPPFramingErrors_Type.__name__=_B
_L2tpSessionClientPPPFramingErrors_Object=MibTableColumn
l2tpSessionClientPPPFramingErrors=_L2tpSessionClientPPPFramingErrors_Object((1,3,6,1,4,1,272,4,23,8,40,10,160),_L2tpSessionClientPPPFramingErrors_Type())
l2tpSessionClientPPPFramingErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionClientPPPFramingErrors.setStatus(_A)
class _L2tpSessionClientPPPHardwareOverruns_Type(Integer32):defaultValue=0
_L2tpSessionClientPPPHardwareOverruns_Type.__name__=_B
_L2tpSessionClientPPPHardwareOverruns_Object=MibTableColumn
l2tpSessionClientPPPHardwareOverruns=_L2tpSessionClientPPPHardwareOverruns_Object((1,3,6,1,4,1,272,4,23,8,40,10,170),_L2tpSessionClientPPPHardwareOverruns_Type())
l2tpSessionClientPPPHardwareOverruns.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionClientPPPHardwareOverruns.setStatus(_A)
class _L2tpSessionClientPPPBufferOverruns_Type(Integer32):defaultValue=0
_L2tpSessionClientPPPBufferOverruns_Type.__name__=_B
_L2tpSessionClientPPPBufferOverruns_Object=MibTableColumn
l2tpSessionClientPPPBufferOverruns=_L2tpSessionClientPPPBufferOverruns_Object((1,3,6,1,4,1,272,4,23,8,40,10,180),_L2tpSessionClientPPPBufferOverruns_Type())
l2tpSessionClientPPPBufferOverruns.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionClientPPPBufferOverruns.setStatus(_A)
class _L2tpSessionClientPPPTimeoutErrors_Type(Integer32):defaultValue=0
_L2tpSessionClientPPPTimeoutErrors_Type.__name__=_B
_L2tpSessionClientPPPTimeoutErrors_Object=MibTableColumn
l2tpSessionClientPPPTimeoutErrors=_L2tpSessionClientPPPTimeoutErrors_Object((1,3,6,1,4,1,272,4,23,8,40,10,190),_L2tpSessionClientPPPTimeoutErrors_Type())
l2tpSessionClientPPPTimeoutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionClientPPPTimeoutErrors.setStatus(_A)
class _L2tpSessionClientPPPAlignmentErrors_Type(Integer32):defaultValue=0
_L2tpSessionClientPPPAlignmentErrors_Type.__name__=_B
_L2tpSessionClientPPPAlignmentErrors_Object=MibTableColumn
l2tpSessionClientPPPAlignmentErrors=_L2tpSessionClientPPPAlignmentErrors_Object((1,3,6,1,4,1,272,4,23,8,40,10,200),_L2tpSessionClientPPPAlignmentErrors_Type())
l2tpSessionClientPPPAlignmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionClientPPPAlignmentErrors.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'bintec':bintec,'bibo':bibo,'vpn':vpn,'l2tp':l2tp,'l2tpGlobals':l2tpGlobals,'l2tpGlobUdpPort':l2tpGlobUdpPort,'l2tpGlobPortUsage':l2tpGlobPortUsage,'l2tpTunnelProfileTable':l2tpTunnelProfileTable,'l2tpTunnelProfileEntry':l2tpTunnelProfileEntry,_I:l2tpTunnelProfileIndex,'l2tpTunnelProfileName':l2tpTunnelProfileName,'l2tpTunnelProfileRemoteIpAddress':l2tpTunnelProfileRemoteIpAddress,'l2tpTunnelProfileRemoteIpAddressBackup':l2tpTunnelProfileRemoteIpAddressBackup,'l2tpTunnelProfileRemoteUdpPort':l2tpTunnelProfileRemoteUdpPort,'l2tpTunnelProfileRemoteHostname':l2tpTunnelProfileRemoteHostname,'l2tpTunnelProfileLocalIpAddress':l2tpTunnelProfileLocalIpAddress,'l2tpTunnelProfileLocalUdpPort':l2tpTunnelProfileLocalUdpPort,'l2tpTunnelProfileLocalHostname':l2tpTunnelProfileLocalHostname,'l2tpTunnelProfilePassword':l2tpTunnelProfilePassword,'l2tpTunnelProfileReceiveWindowSize':l2tpTunnelProfileReceiveWindowSize,'l2tpTunnelProfileHelloInterval':l2tpTunnelProfileHelloInterval,'l2tpTunnelProfileSessionDataSequencing':l2tpTunnelProfileSessionDataSequencing,'l2tpTunnelProfileMinRetryTime':l2tpTunnelProfileMinRetryTime,'l2tpTunnelProfileMaxRetryTime':l2tpTunnelProfileMaxRetryTime,'l2tpTunnelProfileMaxRetries':l2tpTunnelProfileMaxRetries,'l2tpTunnelProfileRadiusAssignment':l2tpTunnelProfileRadiusAssignment,'l2tpTunnelProfileRadiusGroupId':l2tpTunnelProfileRadiusGroupId,'l2tpTunnelTable':l2tpTunnelTable,'l2tpTunnelEntry':l2tpTunnelEntry,'l2tpTunnelRemoteIpAddress':l2tpTunnelRemoteIpAddress,'l2tpTunnelRemoteUdpPort':l2tpTunnelRemoteUdpPort,'l2tpTunnelRemoteTunnelId':l2tpTunnelRemoteTunnelId,'l2tpTunnelRemoteReceiveWindowSize':l2tpTunnelRemoteReceiveWindowSize,'l2tpTunnelRemoteHostname':l2tpTunnelRemoteHostname,'l2tpTunnelRemoteVendorName':l2tpTunnelRemoteVendorName,'l2tpTunnelLocalIpAddress':l2tpTunnelLocalIpAddress,'l2tpTunnelLocalUdpPort':l2tpTunnelLocalUdpPort,_J:l2tpTunnelLocalTunnelId,'l2tpTunnelLocalReceiveWindowSize':l2tpTunnelLocalReceiveWindowSize,'l2tpTunnelLocalHostname':l2tpTunnelLocalHostname,'l2tpTunnelPassword':l2tpTunnelPassword,'l2tpTunnelHelloInterval':l2tpTunnelHelloInterval,'l2tpTunnelSessionDataSequencing':l2tpTunnelSessionDataSequencing,'l2tpTunnelMinRetryTime':l2tpTunnelMinRetryTime,'l2tpTunnelMaxRetryTime':l2tpTunnelMaxRetryTime,'l2tpTunnelMaxRetries':l2tpTunnelMaxRetries,'l2tpTunnelState':l2tpTunnelState,'l2tpSessionTable':l2tpSessionTable,'l2tpSessionEntry':l2tpSessionEntry,'l2tpSessionRemoteIpAddress':l2tpSessionRemoteIpAddress,'l2tpSessionRemoteUdpPort':l2tpSessionRemoteUdpPort,'l2tpSessionRemoteTunnelId':l2tpSessionRemoteTunnelId,'l2tpSessionRemoteSessionId':l2tpSessionRemoteSessionId,'l2tpSessionRemoteHostname':l2tpSessionRemoteHostname,'l2tpSessionLocalIpAddress':l2tpSessionLocalIpAddress,'l2tpSessionLocalUdpPort':l2tpSessionLocalUdpPort,'l2tpSessionLocalTunnelId':l2tpSessionLocalTunnelId,_M:l2tpSessionLocalSessionId,'l2tpSessionLocalHostname':l2tpSessionLocalHostname,'l2tpSessionCallSerialNumber':l2tpSessionCallSerialNumber,'l2tpSessionDataSequencing':l2tpSessionDataSequencing,'l2tpSessionState':l2tpSessionState,'l2tpSessionInfo':l2tpSessionInfo,'l2tpSessionClientPPPCrcErrors':l2tpSessionClientPPPCrcErrors,'l2tpSessionClientPPPFramingErrors':l2tpSessionClientPPPFramingErrors,'l2tpSessionClientPPPHardwareOverruns':l2tpSessionClientPPPHardwareOverruns,'l2tpSessionClientPPPBufferOverruns':l2tpSessionClientPPPBufferOverruns,'l2tpSessionClientPPPTimeoutErrors':l2tpSessionClientPPPTimeoutErrors,'l2tpSessionClientPPPAlignmentErrors':l2tpSessionClientPPPAlignmentErrors})