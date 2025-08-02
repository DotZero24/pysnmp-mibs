_U='alaIND1WebMgtConfigMIBCertGroup'
_T='alaIND1WebMgtNotificationGroup'
_S='alaIND1WebMgtConfigMIBGroup'
_R='webMgtServerErrorTrap'
_Q='alcatelIND1WebMgtCertMD5'
_P='alcatelIND1WebMgtCertFile'
_O='alaIND1WebMgtServerError'
_N='alaIND1WebMgtServerStatus'
_M='alaIND1WebMgtHttpsPort'
_L='alaIND1WebMgtHttpPort'
_K='alaIND1WebMgtSSL'
_J='alaIND1WebMgtAdminStatus'
_I='read-only'
_H='webMgtServerError'
_G='disable'
_F='enable'
_E='SnmpAdminString'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-WEBMGT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1WebMgt,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1WebMgt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1WebMgtMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1))
if mibBuilder.loadTexts:alcatelIND1WebMgtMIB.setRevisions(('2010-05-13 00:00',))
_AlcatelIND1WebMgtMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1WebMgtMIBNotifications=_AlcatelIND1WebMgtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1,0))
if mibBuilder.loadTexts:alcatelIND1WebMgtMIBNotifications.setStatus(_A)
_AlcatelIND1WebMgtMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1WebMgtMIBObjects=_AlcatelIND1WebMgtMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1,1))
if mibBuilder.loadTexts:alcatelIND1WebMgtMIBObjects.setStatus(_A)
class _AlaIND1WebMgtAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaIND1WebMgtAdminStatus_Type.__name__=_C
_AlaIND1WebMgtAdminStatus_Object=MibScalar
alaIND1WebMgtAdminStatus=_AlaIND1WebMgtAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,1),_AlaIND1WebMgtAdminStatus_Type())
alaIND1WebMgtAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIND1WebMgtAdminStatus.setStatus(_A)
class _AlaIND1WebMgtSSL_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaIND1WebMgtSSL_Type.__name__=_C
_AlaIND1WebMgtSSL_Object=MibScalar
alaIND1WebMgtSSL=_AlaIND1WebMgtSSL_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,2),_AlaIND1WebMgtSSL_Type())
alaIND1WebMgtSSL.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIND1WebMgtSSL.setStatus(_A)
class _AlaIND1WebMgtHttpPort_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(80,80),ValueRangeConstraint(1024,65535))
_AlaIND1WebMgtHttpPort_Type.__name__=_C
_AlaIND1WebMgtHttpPort_Object=MibScalar
alaIND1WebMgtHttpPort=_AlaIND1WebMgtHttpPort_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,3),_AlaIND1WebMgtHttpPort_Type())
alaIND1WebMgtHttpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIND1WebMgtHttpPort.setStatus(_A)
class _AlaIND1WebMgtHttpsPort_Type(Integer32):defaultValue=443;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(443,443),ValueRangeConstraint(1024,65535))
_AlaIND1WebMgtHttpsPort_Type.__name__=_C
_AlaIND1WebMgtHttpsPort_Object=MibScalar
alaIND1WebMgtHttpsPort=_AlaIND1WebMgtHttpsPort_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,4),_AlaIND1WebMgtHttpsPort_Type())
alaIND1WebMgtHttpsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIND1WebMgtHttpsPort.setStatus(_A)
class _AlaIND1WebMgtServerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),('restarting',3),('error',4)))
_AlaIND1WebMgtServerStatus_Type.__name__=_C
_AlaIND1WebMgtServerStatus_Object=MibScalar
alaIND1WebMgtServerStatus=_AlaIND1WebMgtServerStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,5),_AlaIND1WebMgtServerStatus_Type())
alaIND1WebMgtServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIND1WebMgtServerStatus.setStatus(_A)
class _AlaIND1WebMgtServerError_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AlaIND1WebMgtServerError_Type.__name__=_E
_AlaIND1WebMgtServerError_Object=MibScalar
alaIND1WebMgtServerError=_AlaIND1WebMgtServerError_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,6),_AlaIND1WebMgtServerError_Type())
alaIND1WebMgtServerError.setMaxAccess(_I)
if mibBuilder.loadTexts:alaIND1WebMgtServerError.setStatus(_A)
_WebMgtTrapsObj_ObjectIdentity=ObjectIdentity
webMgtTrapsObj=_WebMgtTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,7))
class _WebMgtServerError_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WebMgtServerError_Type.__name__=_E
_WebMgtServerError_Object=MibScalar
webMgtServerError=_WebMgtServerError_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,7,1),_WebMgtServerError_Type())
webMgtServerError.setMaxAccess(_I)
if mibBuilder.loadTexts:webMgtServerError.setStatus(_A)
_AlcatelIND1WebMgtCertObjects_ObjectIdentity=ObjectIdentity
alcatelIND1WebMgtCertObjects=_AlcatelIND1WebMgtCertObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,8))
if mibBuilder.loadTexts:alcatelIND1WebMgtCertObjects.setStatus(_A)
class _AlcatelIND1WebMgtCertFile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('default',2),('user',3)))
_AlcatelIND1WebMgtCertFile_Type.__name__=_C
_AlcatelIND1WebMgtCertFile_Object=MibScalar
alcatelIND1WebMgtCertFile=_AlcatelIND1WebMgtCertFile_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,8,1),_AlcatelIND1WebMgtCertFile_Type())
alcatelIND1WebMgtCertFile.setMaxAccess(_D)
if mibBuilder.loadTexts:alcatelIND1WebMgtCertFile.setStatus(_A)
class _AlcatelIND1WebMgtCertMD5_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlcatelIND1WebMgtCertMD5_Type.__name__=_E
_AlcatelIND1WebMgtCertMD5_Object=MibScalar
alcatelIND1WebMgtCertMD5=_AlcatelIND1WebMgtCertMD5_Object((1,3,6,1,4,1,6486,801,1,2,1,17,1,1,8,2),_AlcatelIND1WebMgtCertMD5_Type())
alcatelIND1WebMgtCertMD5.setMaxAccess(_D)
if mibBuilder.loadTexts:alcatelIND1WebMgtCertMD5.setStatus(_A)
_AlcatelIND1WebMgtMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1WebMgtMIBConformance=_AlcatelIND1WebMgtMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1,2))
if mibBuilder.loadTexts:alcatelIND1WebMgtMIBConformance.setStatus(_A)
_AlcatelIND1WebMgtMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1WebMgtMIBGroups=_AlcatelIND1WebMgtMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1,2,1))
if mibBuilder.loadTexts:alcatelIND1WebMgtMIBGroups.setStatus(_A)
_AlcatelIND1WebMgtMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1WebMgtMIBCompliances=_AlcatelIND1WebMgtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17,1,2,2))
if mibBuilder.loadTexts:alcatelIND1WebMgtMIBCompliances.setStatus(_A)
alaIND1WebMgtConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,17,1,2,1,1))
alaIND1WebMgtConfigMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_H)))
if mibBuilder.loadTexts:alaIND1WebMgtConfigMIBGroup.setStatus(_A)
alaIND1WebMgtConfigMIBCertGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,17,1,2,1,3))
alaIND1WebMgtConfigMIBCertGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:alaIND1WebMgtConfigMIBCertGroup.setStatus(_A)
webMgtServerErrorTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,17,1,0,1))
webMgtServerErrorTrap.setObjects((_B,_H))
if mibBuilder.loadTexts:webMgtServerErrorTrap.setStatus(_A)
alaIND1WebMgtNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,17,1,2,1,2))
alaIND1WebMgtNotificationGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:alaIND1WebMgtNotificationGroup.setStatus(_A)
alaIND1WebMgtConfigMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,17,1,2,2,1))
alaIND1WebMgtConfigMIBCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alaIND1WebMgtConfigMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1WebMgtMIB':alcatelIND1WebMgtMIB,'alcatelIND1WebMgtMIBNotifications':alcatelIND1WebMgtMIBNotifications,_R:webMgtServerErrorTrap,'alcatelIND1WebMgtMIBObjects':alcatelIND1WebMgtMIBObjects,_J:alaIND1WebMgtAdminStatus,_K:alaIND1WebMgtSSL,_L:alaIND1WebMgtHttpPort,_M:alaIND1WebMgtHttpsPort,_N:alaIND1WebMgtServerStatus,_O:alaIND1WebMgtServerError,'webMgtTrapsObj':webMgtTrapsObj,_H:webMgtServerError,'alcatelIND1WebMgtCertObjects':alcatelIND1WebMgtCertObjects,_P:alcatelIND1WebMgtCertFile,_Q:alcatelIND1WebMgtCertMD5,'alcatelIND1WebMgtMIBConformance':alcatelIND1WebMgtMIBConformance,'alcatelIND1WebMgtMIBGroups':alcatelIND1WebMgtMIBGroups,_S:alaIND1WebMgtConfigMIBGroup,_T:alaIND1WebMgtNotificationGroup,_U:alaIND1WebMgtConfigMIBCertGroup,'alcatelIND1WebMgtMIBCompliances':alcatelIND1WebMgtMIBCompliances,'alaIND1WebMgtConfigMIBCompliance':alaIND1WebMgtConfigMIBCompliance})