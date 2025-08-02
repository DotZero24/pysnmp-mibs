_Y='sntpServerGroupVer1'
_X='sntpBasicGroupVer1'
_W='sntpStaticPort'
_V='sntpStaticHost'
_U='sntpSelectConfigSource'
_T='sntpPort'
_S='sntpHost'
_R='sntpConfigSource'
_Q='sntpTimeZoneStringIsValid'
_P='sntpTimeZoneString'
_O='sntpSynchronizationPeriodOnError'
_N='sntpSynchronizationPeriod'
_M='sntpEnable'
_L='192.168.0.10'
_K='MxIpSelectConfigSource'
_J='MxIpConfigSource'
_I='OctetString'
_H='Unsigned32'
_G='Integer32'
_F='MxIpPort'
_E='MxIpHostName'
_D='read-only'
_C='read-write'
_B='current'
_A='MX-SNTP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,ipAddressStatus,mediatrixConfig=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixConfig')
MxIpConfigSource,MxIpHostName,MxIpPort,MxIpSelectConfigSource=mibBuilder.importSymbols('MX-TC',_J,_E,_F,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sntpMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,65))
if mibBuilder.loadTexts:sntpMIB.setRevisions(('1907-10-24 00:00','1903-02-24 00:00'))
_IpAddressStatusSntp_ObjectIdentity=ObjectIdentity
ipAddressStatusSntp=_IpAddressStatusSntp_ObjectIdentity((1,3,6,1,4,1,4935,10,1,80))
class _SntpConfigSource_Type(MxIpConfigSource):defaultValue=1
_SntpConfigSource_Type.__name__=_J
_SntpConfigSource_Object=MibScalar
sntpConfigSource=_SntpConfigSource_Object((1,3,6,1,4,1,4935,10,1,80,1),_SntpConfigSource_Type())
sntpConfigSource.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpConfigSource.setStatus(_B)
class _SntpHost_Type(MxIpHostName):defaultValue=OctetString(_L)
_SntpHost_Type.__name__=_E
_SntpHost_Object=MibScalar
sntpHost=_SntpHost_Object((1,3,6,1,4,1,4935,10,1,80,10),_SntpHost_Type())
sntpHost.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpHost.setStatus(_B)
class _SntpPort_Type(MxIpPort):defaultValue=123
_SntpPort_Type.__name__=_F
_SntpPort_Object=MibScalar
sntpPort=_SntpPort_Object((1,3,6,1,4,1,4935,10,1,80,11),_SntpPort_Type())
sntpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpPort.setStatus(_B)
_IpAddressConfigSntp_ObjectIdentity=ObjectIdentity
ipAddressConfigSntp=_IpAddressConfigSntp_ObjectIdentity((1,3,6,1,4,1,4935,15,1,80))
class _SntpSelectConfigSource_Type(MxIpSelectConfigSource):defaultValue=1
_SntpSelectConfigSource_Type.__name__=_K
_SntpSelectConfigSource_Object=MibScalar
sntpSelectConfigSource=_SntpSelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,80,1),_SntpSelectConfigSource_Type())
sntpSelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpSelectConfigSource.setStatus(_B)
_IpAddressConfigSntpStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigSntpStatic=_IpAddressConfigSntpStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,80,10))
class _SntpStaticHost_Type(MxIpHostName):defaultValue=OctetString(_L)
_SntpStaticHost_Type.__name__=_E
_SntpStaticHost_Object=MibScalar
sntpStaticHost=_SntpStaticHost_Object((1,3,6,1,4,1,4935,15,1,80,10,10),_SntpStaticHost_Type())
sntpStaticHost.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpStaticHost.setStatus(_B)
class _SntpStaticPort_Type(MxIpPort):defaultValue=123
_SntpStaticPort_Type.__name__=_F
_SntpStaticPort_Object=MibScalar
sntpStaticPort=_SntpStaticPort_Object((1,3,6,1,4,1,4935,15,1,80,10,11),_SntpStaticPort_Type())
sntpStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpStaticPort.setStatus(_B)
_SntpMIBObjects_ObjectIdentity=ObjectIdentity
sntpMIBObjects=_SntpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,65,1))
class _SntpEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_SntpEnable_Type.__name__=_G
_SntpEnable_Object=MibScalar
sntpEnable=_SntpEnable_Object((1,3,6,1,4,1,4935,15,65,1,5),_SntpEnable_Type())
sntpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpEnable.setStatus(_B)
class _SntpSynchronizationPeriod_Type(Unsigned32):defaultValue=1440;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_SntpSynchronizationPeriod_Type.__name__=_H
_SntpSynchronizationPeriod_Object=MibScalar
sntpSynchronizationPeriod=_SntpSynchronizationPeriod_Object((1,3,6,1,4,1,4935,15,65,1,10),_SntpSynchronizationPeriod_Type())
sntpSynchronizationPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpSynchronizationPeriod.setStatus(_B)
class _SntpSynchronizationPeriodOnError_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_SntpSynchronizationPeriodOnError_Type.__name__=_H
_SntpSynchronizationPeriodOnError_Object=MibScalar
sntpSynchronizationPeriodOnError=_SntpSynchronizationPeriodOnError_Object((1,3,6,1,4,1,4935,15,65,1,15),_SntpSynchronizationPeriodOnError_Type())
sntpSynchronizationPeriodOnError.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpSynchronizationPeriodOnError.setStatus(_B)
_SntpTimeZoneConfig_ObjectIdentity=ObjectIdentity
sntpTimeZoneConfig=_SntpTimeZoneConfig_ObjectIdentity((1,3,6,1,4,1,4935,15,65,1,25))
class _SntpTimeZoneString_Type(OctetString):defaultValue=OctetString('EST5DST4,M3.2.0/02:00:00,M11.1.0/02:00:00');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SntpTimeZoneString_Type.__name__=_I
_SntpTimeZoneString_Object=MibScalar
sntpTimeZoneString=_SntpTimeZoneString_Object((1,3,6,1,4,1,4935,15,65,1,25,15),_SntpTimeZoneString_Type())
sntpTimeZoneString.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpTimeZoneString.setStatus(_B)
class _SntpTimeZoneStringIsValid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('valid',1)))
_SntpTimeZoneStringIsValid_Type.__name__=_G
_SntpTimeZoneStringIsValid_Object=MibScalar
sntpTimeZoneStringIsValid=_SntpTimeZoneStringIsValid_Object((1,3,6,1,4,1,4935,15,65,1,25,20),_SntpTimeZoneStringIsValid_Type())
sntpTimeZoneStringIsValid.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpTimeZoneStringIsValid.setStatus('deprecated')
_SntpConformance_ObjectIdentity=ObjectIdentity
sntpConformance=_SntpConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,65,2))
_SntpCompliances_ObjectIdentity=ObjectIdentity
sntpCompliances=_SntpCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,65,2,1))
_SntpGroups_ObjectIdentity=ObjectIdentity
sntpGroups=_SntpGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,65,2,2))
sntpBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,65,2,2,1))
sntpBasicGroupVer1.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:sntpBasicGroupVer1.setStatus(_B)
sntpServerGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,65,2,2,2))
sntpServerGroupVer1.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:sntpServerGroupVer1.setStatus(_B)
sntpBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,65,2,1,1))
sntpBasicComplVer1.setObjects(*((_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:sntpBasicComplVer1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ipAddressStatusSntp':ipAddressStatusSntp,_R:sntpConfigSource,_S:sntpHost,_T:sntpPort,'ipAddressConfigSntp':ipAddressConfigSntp,_U:sntpSelectConfigSource,'ipAddressConfigSntpStatic':ipAddressConfigSntpStatic,_V:sntpStaticHost,_W:sntpStaticPort,'sntpMIB':sntpMIB,'sntpMIBObjects':sntpMIBObjects,_M:sntpEnable,_N:sntpSynchronizationPeriod,_O:sntpSynchronizationPeriodOnError,'sntpTimeZoneConfig':sntpTimeZoneConfig,_P:sntpTimeZoneString,_Q:sntpTimeZoneStringIsValid,'sntpConformance':sntpConformance,'sntpCompliances':sntpCompliances,'sntpBasicComplVer1':sntpBasicComplVer1,'sntpGroups':sntpGroups,_X:sntpBasicGroupVer1,_Y:sntpServerGroupVer1})