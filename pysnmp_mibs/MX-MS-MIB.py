_i='msBasicNotificationGroupVer1'
_h='msServerGroupVer1'
_g='msBasicGroupVer1'
_f='msTrapStatusConfigFile'
_e='msTrapStatusInformation'
_d='msTrapConfigInformation'
_c='msDhcpSiteSpecificCode'
_b='msStaticTrapPort'
_a='msStaticHost'
_Z='msSelectConfigSource'
_Y='msTrapPort'
_X='msHost'
_W='msConfigSource'
_V='msTrapRetransmissionRetryCount'
_U='msTrapRetransmissionPeriod'
_T='msEnable'
_S='192.168.0.10'
_R='Unsigned32'
_Q='sysObjectID'
_P='SNMPv2-MIB'
_O='MxIpSelectConfigSource'
_N='MxIpDhcpSiteSpecificCode'
_M='MxIpConfigSource'
_L='sysConfigDownloadConfigMode'
_K='read-only'
_J='Integer32'
_I='MxIpPort'
_H='MxIpHostName'
_G='sysConfigDownloadConfigFile'
_F='sysMacAddress'
_E='MX-SYSTEM-MGMT-MIB'
_D='MX-SYSTEM-CONFIG-MIB'
_C='read-write'
_B='MX-MS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,ipAddressStatus,mediatrixConfig=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixConfig')
sysConfigDownloadConfigFile,sysConfigDownloadConfigMode=mibBuilder.importSymbols(_D,_G,_L)
sysMacAddress,=mibBuilder.importSymbols(_E,_F)
MxIpConfigSource,MxIpDhcpSiteSpecificCode,MxIpHostName,MxIpPort,MxIpSelectConfigSource=mibBuilder.importSymbols('MX-TC',_M,_N,_H,_I,_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysObjectID,=mibBuilder.importSymbols(_P,_Q)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
msMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,15))
if mibBuilder.loadTexts:msMIB.setRevisions(('2004-05-25 00:00','1903-11-11 00:00'))
_IpAddressStatusMs_ObjectIdentity=ObjectIdentity
ipAddressStatusMs=_IpAddressStatusMs_ObjectIdentity((1,3,6,1,4,1,4935,10,1,10))
class _MsConfigSource_Type(MxIpConfigSource):defaultValue=1
_MsConfigSource_Type.__name__=_M
_MsConfigSource_Object=MibScalar
msConfigSource=_MsConfigSource_Object((1,3,6,1,4,1,4935,10,1,10,1),_MsConfigSource_Type())
msConfigSource.setMaxAccess(_K)
if mibBuilder.loadTexts:msConfigSource.setStatus(_A)
class _MsHost_Type(MxIpHostName):defaultValue=OctetString(_S)
_MsHost_Type.__name__=_H
_MsHost_Object=MibScalar
msHost=_MsHost_Object((1,3,6,1,4,1,4935,10,1,10,2),_MsHost_Type())
msHost.setMaxAccess(_K)
if mibBuilder.loadTexts:msHost.setStatus(_A)
class _MsTrapPort_Type(MxIpPort):defaultValue=162
_MsTrapPort_Type.__name__=_I
_MsTrapPort_Object=MibScalar
msTrapPort=_MsTrapPort_Object((1,3,6,1,4,1,4935,10,1,10,3),_MsTrapPort_Type())
msTrapPort.setMaxAccess(_K)
if mibBuilder.loadTexts:msTrapPort.setStatus(_A)
_IpAddressConfigMs_ObjectIdentity=ObjectIdentity
ipAddressConfigMs=_IpAddressConfigMs_ObjectIdentity((1,3,6,1,4,1,4935,15,1,10))
class _MsSelectConfigSource_Type(MxIpSelectConfigSource):defaultValue=1
_MsSelectConfigSource_Type.__name__=_O
_MsSelectConfigSource_Object=MibScalar
msSelectConfigSource=_MsSelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,10,1),_MsSelectConfigSource_Type())
msSelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:msSelectConfigSource.setStatus(_A)
_IpAddressConfigMsStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigMsStatic=_IpAddressConfigMsStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,10,10))
class _MsStaticHost_Type(MxIpHostName):defaultValue=OctetString(_S)
_MsStaticHost_Type.__name__=_H
_MsStaticHost_Object=MibScalar
msStaticHost=_MsStaticHost_Object((1,3,6,1,4,1,4935,15,1,10,10,1),_MsStaticHost_Type())
msStaticHost.setMaxAccess(_C)
if mibBuilder.loadTexts:msStaticHost.setStatus(_A)
class _MsStaticTrapPort_Type(MxIpPort):defaultValue=162
_MsStaticTrapPort_Type.__name__=_I
_MsStaticTrapPort_Object=MibScalar
msStaticTrapPort=_MsStaticTrapPort_Object((1,3,6,1,4,1,4935,15,1,10,10,2),_MsStaticTrapPort_Type())
msStaticTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:msStaticTrapPort.setStatus(_A)
_IpAddressConfigMsDhcp_ObjectIdentity=ObjectIdentity
ipAddressConfigMsDhcp=_IpAddressConfigMsDhcp_ObjectIdentity((1,3,6,1,4,1,4935,15,1,10,30))
class _MsDhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):defaultValue=0
_MsDhcpSiteSpecificCode_Type.__name__=_N
_MsDhcpSiteSpecificCode_Object=MibScalar
msDhcpSiteSpecificCode=_MsDhcpSiteSpecificCode_Object((1,3,6,1,4,1,4935,15,1,10,30,1),_MsDhcpSiteSpecificCode_Type())
msDhcpSiteSpecificCode.setMaxAccess(_C)
if mibBuilder.loadTexts:msDhcpSiteSpecificCode.setStatus(_A)
_MsMIBObjects_ObjectIdentity=ObjectIdentity
msMIBObjects=_MsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,15,1))
class _MsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_MsEnable_Type.__name__=_J
_MsEnable_Object=MibScalar
msEnable=_MsEnable_Object((1,3,6,1,4,1,4935,15,15,1,5),_MsEnable_Type())
msEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:msEnable.setStatus(_A)
class _MsTrapRetransmissionPeriod_Type(Unsigned32):defaultValue=60000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,604800000))
_MsTrapRetransmissionPeriod_Type.__name__=_R
_MsTrapRetransmissionPeriod_Object=MibScalar
msTrapRetransmissionPeriod=_MsTrapRetransmissionPeriod_Object((1,3,6,1,4,1,4935,15,15,1,20),_MsTrapRetransmissionPeriod_Type())
msTrapRetransmissionPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:msTrapRetransmissionPeriod.setStatus(_A)
class _MsTrapRetransmissionRetryCount_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MsTrapRetransmissionRetryCount_Type.__name__=_J
_MsTrapRetransmissionRetryCount_Object=MibScalar
msTrapRetransmissionRetryCount=_MsTrapRetransmissionRetryCount_Object((1,3,6,1,4,1,4935,15,15,1,21),_MsTrapRetransmissionRetryCount_Type())
msTrapRetransmissionRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:msTrapRetransmissionRetryCount.setStatus(_A)
_MsConformance_ObjectIdentity=ObjectIdentity
msConformance=_MsConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,15,2))
_MsCompliances_ObjectIdentity=ObjectIdentity
msCompliances=_MsCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,15,2,1))
_MsGroups_ObjectIdentity=ObjectIdentity
msGroups=_MsGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,15,2,2))
_MsEvents_ObjectIdentity=ObjectIdentity
msEvents=_MsEvents_ObjectIdentity((1,3,6,1,4,1,4935,15,15,3))
_MsNotifications_ObjectIdentity=ObjectIdentity
msNotifications=_MsNotifications_ObjectIdentity((1,3,6,1,4,1,4935,15,15,3,2))
msBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,15,2,2,1))
msBasicGroupVer1.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:msBasicGroupVer1.setStatus(_A)
msServerGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,15,2,2,2))
msServerGroupVer1.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:msServerGroupVer1.setStatus(_A)
msTrapConfigInformation=NotificationType((1,3,6,1,4,1,4935,15,15,3,2,700))
msTrapConfigInformation.setObjects(*((_P,_Q),(_E,_F),(_D,_G)))
if mibBuilder.loadTexts:msTrapConfigInformation.setStatus(_A)
msTrapStatusInformation=NotificationType((1,3,6,1,4,1,4935,15,15,3,2,800))
msTrapStatusInformation.setObjects(*((_E,_F),(_D,_L)))
if mibBuilder.loadTexts:msTrapStatusInformation.setStatus(_A)
msTrapStatusConfigFile=NotificationType((1,3,6,1,4,1,4935,15,15,3,2,900))
msTrapStatusConfigFile.setObjects(*((_E,_F),(_D,_G)))
if mibBuilder.loadTexts:msTrapStatusConfigFile.setStatus(_A)
msBasicNotificationGroupVer1=NotificationGroup((1,3,6,1,4,1,4935,15,15,2,2,3))
msBasicNotificationGroupVer1.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:msBasicNotificationGroupVer1.setStatus(_A)
msBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,15,2,1,1))
msBasicComplVer1.setObjects(*((_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:msBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusMs':ipAddressStatusMs,_W:msConfigSource,_X:msHost,_Y:msTrapPort,'ipAddressConfigMs':ipAddressConfigMs,_Z:msSelectConfigSource,'ipAddressConfigMsStatic':ipAddressConfigMsStatic,_a:msStaticHost,_b:msStaticTrapPort,'ipAddressConfigMsDhcp':ipAddressConfigMsDhcp,_c:msDhcpSiteSpecificCode,'msMIB':msMIB,'msMIBObjects':msMIBObjects,_T:msEnable,_U:msTrapRetransmissionPeriod,_V:msTrapRetransmissionRetryCount,'msConformance':msConformance,'msCompliances':msCompliances,'msBasicComplVer1':msBasicComplVer1,'msGroups':msGroups,_g:msBasicGroupVer1,_h:msServerGroupVer1,_i:msBasicNotificationGroupVer1,'msEvents':msEvents,'msNotifications':msNotifications,_d:msTrapConfigInformation,_e:msTrapStatusInformation,_f:msTrapStatusConfigFile})