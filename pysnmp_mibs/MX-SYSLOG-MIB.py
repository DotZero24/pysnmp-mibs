_m='syslogMsgCustomizationGroupVer1'
_l='syslogServerGroupVer1'
_k='syslogBasicGroupVer1'
_j='syslogMsgDisplayLocalHost'
_i='syslogMsgDisplayTimeFormat'
_h='syslogMsgDisplayTime'
_g='syslogMsgDisplayMacAddress'
_f='syslogDhcpSiteSpecificCode'
_e='syslogStaticPort'
_d='syslogStaticHost'
_c='syslogSelectConfigSource'
_b='syslogPort'
_a='syslogHost'
_Z='syslogConfigSource'
_Y='syslogMsgLocalMsg'
_X='syslogMsgLocalModule'
_W='syslogMsgLocalSeverity'
_V='syslogMsgLocalTime'
_U='syslogMsgLocalMaxNbr'
_T='syslogMsgLocalMaxSeverity'
_S='syslogMsgMaxSeverity'
_R='informational'
_Q='warning'
_P='critical'
_O='disabled'
_N='192.168.0.10'
_M='Unsigned32'
_L='MxIpSelectConfigSource'
_K='MxIpDhcpSiteSpecificCode'
_J='MxIpConfigSource'
_I='MxIpPort'
_H='MxIpHostName'
_G='Integer32'
_F='MxEnableState'
_E='OctetString'
_D='read-only'
_C='read-write'
_B='MX-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,ipAddressStatus,mediatrixConfig=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixConfig')
MxEnableState,MxIpConfigSource,MxIpDhcpSiteSpecificCode,MxIpHostName,MxIpPort,MxIpSelectConfigSource=mibBuilder.importSymbols('MX-TC',_F,_J,_K,_H,_I,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
syslogMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,17))
if mibBuilder.loadTexts:syslogMIB.setRevisions(('2004-11-05 00:00','2004-04-27 00:00','2004-02-09 00:00','2002-08-23 00:00','2001-08-06 00:00'))
_IpAddressStatusSyslog_ObjectIdentity=ObjectIdentity
ipAddressStatusSyslog=_IpAddressStatusSyslog_ObjectIdentity((1,3,6,1,4,1,4935,10,1,20))
class _SyslogConfigSource_Type(MxIpConfigSource):defaultValue=1
_SyslogConfigSource_Type.__name__=_J
_SyslogConfigSource_Object=MibScalar
syslogConfigSource=_SyslogConfigSource_Object((1,3,6,1,4,1,4935,10,1,20,1),_SyslogConfigSource_Type())
syslogConfigSource.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogConfigSource.setStatus(_A)
class _SyslogHost_Type(MxIpHostName):defaultValue=OctetString(_N)
_SyslogHost_Type.__name__=_H
_SyslogHost_Object=MibScalar
syslogHost=_SyslogHost_Object((1,3,6,1,4,1,4935,10,1,20,2),_SyslogHost_Type())
syslogHost.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogHost.setStatus(_A)
class _SyslogPort_Type(MxIpPort):defaultValue=514
_SyslogPort_Type.__name__=_I
_SyslogPort_Object=MibScalar
syslogPort=_SyslogPort_Object((1,3,6,1,4,1,4935,10,1,20,3),_SyslogPort_Type())
syslogPort.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogPort.setStatus(_A)
_IpAddressConfigSyslog_ObjectIdentity=ObjectIdentity
ipAddressConfigSyslog=_IpAddressConfigSyslog_ObjectIdentity((1,3,6,1,4,1,4935,15,1,20))
class _SyslogSelectConfigSource_Type(MxIpSelectConfigSource):defaultValue=1
_SyslogSelectConfigSource_Type.__name__=_L
_SyslogSelectConfigSource_Object=MibScalar
syslogSelectConfigSource=_SyslogSelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,20,1),_SyslogSelectConfigSource_Type())
syslogSelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogSelectConfigSource.setStatus(_A)
_IpAddressConfigSyslogStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigSyslogStatic=_IpAddressConfigSyslogStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,20,10))
class _SyslogStaticHost_Type(MxIpHostName):defaultValue=OctetString(_N)
_SyslogStaticHost_Type.__name__=_H
_SyslogStaticHost_Object=MibScalar
syslogStaticHost=_SyslogStaticHost_Object((1,3,6,1,4,1,4935,15,1,20,10,1),_SyslogStaticHost_Type())
syslogStaticHost.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogStaticHost.setStatus(_A)
class _SyslogStaticPort_Type(MxIpPort):defaultValue=514
_SyslogStaticPort_Type.__name__=_I
_SyslogStaticPort_Object=MibScalar
syslogStaticPort=_SyslogStaticPort_Object((1,3,6,1,4,1,4935,15,1,20,10,2),_SyslogStaticPort_Type())
syslogStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogStaticPort.setStatus(_A)
_IpAddressConfigSyslogDhcp_ObjectIdentity=ObjectIdentity
ipAddressConfigSyslogDhcp=_IpAddressConfigSyslogDhcp_ObjectIdentity((1,3,6,1,4,1,4935,15,1,20,30))
class _SyslogDhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):defaultValue=0
_SyslogDhcpSiteSpecificCode_Type.__name__=_K
_SyslogDhcpSiteSpecificCode_Object=MibScalar
syslogDhcpSiteSpecificCode=_SyslogDhcpSiteSpecificCode_Object((1,3,6,1,4,1,4935,15,1,20,30,1),_SyslogDhcpSiteSpecificCode_Type())
syslogDhcpSiteSpecificCode.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogDhcpSiteSpecificCode.setStatus(_A)
_SyslogMIBObjects_ObjectIdentity=ObjectIdentity
syslogMIBObjects=_SyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,17,1))
class _SyslogMsgMaxSeverity_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),(_P,1),('error',2),(_Q,3),(_R,4),('debug',5)))
_SyslogMsgMaxSeverity_Type.__name__=_G
_SyslogMsgMaxSeverity_Object=MibScalar
syslogMsgMaxSeverity=_SyslogMsgMaxSeverity_Object((1,3,6,1,4,1,4935,15,17,1,5),_SyslogMsgMaxSeverity_Type())
syslogMsgMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgMaxSeverity.setStatus(_A)
class _SyslogMsgLocalMaxSeverity_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),(_P,1),('error',2),(_Q,3),(_R,4),('debug',5)))
_SyslogMsgLocalMaxSeverity_Type.__name__=_G
_SyslogMsgLocalMaxSeverity_Object=MibScalar
syslogMsgLocalMaxSeverity=_SyslogMsgLocalMaxSeverity_Object((1,3,6,1,4,1,4935,15,17,1,50),_SyslogMsgLocalMaxSeverity_Type())
syslogMsgLocalMaxSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgLocalMaxSeverity.setStatus(_A)
class _SyslogMsgLocalMaxNbr_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SyslogMsgLocalMaxNbr_Type.__name__=_M
_SyslogMsgLocalMaxNbr_Object=MibScalar
syslogMsgLocalMaxNbr=_SyslogMsgLocalMaxNbr_Object((1,3,6,1,4,1,4935,15,17,1,100),_SyslogMsgLocalMaxNbr_Type())
syslogMsgLocalMaxNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgLocalMaxNbr.setStatus(_A)
_SyslogLocalMsgTable_Object=MibTable
syslogLocalMsgTable=_SyslogLocalMsgTable_Object((1,3,6,1,4,1,4935,15,17,1,150))
if mibBuilder.loadTexts:syslogLocalMsgTable.setStatus(_A)
_SyslogLocalMsgEntry_Object=MibTableRow
syslogLocalMsgEntry=_SyslogLocalMsgEntry_Object((1,3,6,1,4,1,4935,15,17,1,150,50))
syslogLocalMsgEntry.setIndexNames((0,_B,'ifIndex'))
if mibBuilder.loadTexts:syslogLocalMsgEntry.setStatus(_A)
class _SyslogMsgLocalSeverity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SyslogMsgLocalSeverity_Type.__name__=_E
_SyslogMsgLocalSeverity_Object=MibTableColumn
syslogMsgLocalSeverity=_SyslogMsgLocalSeverity_Object((1,3,6,1,4,1,4935,15,17,1,150,50,50),_SyslogMsgLocalSeverity_Type())
syslogMsgLocalSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgLocalSeverity.setStatus(_A)
class _SyslogMsgLocalTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SyslogMsgLocalTime_Type.__name__=_E
_SyslogMsgLocalTime_Object=MibTableColumn
syslogMsgLocalTime=_SyslogMsgLocalTime_Object((1,3,6,1,4,1,4935,15,17,1,150,50,100),_SyslogMsgLocalTime_Type())
syslogMsgLocalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgLocalTime.setStatus(_A)
class _SyslogMsgLocalModule_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SyslogMsgLocalModule_Type.__name__=_E
_SyslogMsgLocalModule_Object=MibTableColumn
syslogMsgLocalModule=_SyslogMsgLocalModule_Object((1,3,6,1,4,1,4935,15,17,1,150,50,150),_SyslogMsgLocalModule_Type())
syslogMsgLocalModule.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgLocalModule.setStatus(_A)
class _SyslogMsgLocalMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SyslogMsgLocalMsg_Type.__name__=_E
_SyslogMsgLocalMsg_Object=MibTableColumn
syslogMsgLocalMsg=_SyslogMsgLocalMsg_Object((1,3,6,1,4,1,4935,15,17,1,150,50,200),_SyslogMsgLocalMsg_Type())
syslogMsgLocalMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgLocalMsg.setStatus(_A)
_SyslogMsgCustomization_ObjectIdentity=ObjectIdentity
syslogMsgCustomization=_SyslogMsgCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,17,1,200))
class _SyslogMsgDisplayMacAddress_Type(MxEnableState):defaultValue=0
_SyslogMsgDisplayMacAddress_Type.__name__=_F
_SyslogMsgDisplayMacAddress_Object=MibScalar
syslogMsgDisplayMacAddress=_SyslogMsgDisplayMacAddress_Object((1,3,6,1,4,1,4935,15,17,1,200,50),_SyslogMsgDisplayMacAddress_Type())
syslogMsgDisplayMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgDisplayMacAddress.setStatus(_A)
class _SyslogMsgDisplayTime_Type(MxEnableState):defaultValue=1
_SyslogMsgDisplayTime_Type.__name__=_F
_SyslogMsgDisplayTime_Object=MibScalar
syslogMsgDisplayTime=_SyslogMsgDisplayTime_Object((1,3,6,1,4,1,4935,15,17,1,200,150),_SyslogMsgDisplayTime_Type())
syslogMsgDisplayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgDisplayTime.setStatus(_A)
class _SyslogMsgDisplayTimeFormat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pseudoRfcFormat',0),('trueRfcFormat',1)))
_SyslogMsgDisplayTimeFormat_Type.__name__=_G
_SyslogMsgDisplayTimeFormat_Object=MibScalar
syslogMsgDisplayTimeFormat=_SyslogMsgDisplayTimeFormat_Object((1,3,6,1,4,1,4935,15,17,1,200,175),_SyslogMsgDisplayTimeFormat_Type())
syslogMsgDisplayTimeFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgDisplayTimeFormat.setStatus(_A)
class _SyslogMsgDisplayLocalHost_Type(MxEnableState):defaultValue=1
_SyslogMsgDisplayLocalHost_Type.__name__=_F
_SyslogMsgDisplayLocalHost_Object=MibScalar
syslogMsgDisplayLocalHost=_SyslogMsgDisplayLocalHost_Object((1,3,6,1,4,1,4935,15,17,1,200,200),_SyslogMsgDisplayLocalHost_Type())
syslogMsgDisplayLocalHost.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgDisplayLocalHost.setStatus(_A)
_SyslogConformance_ObjectIdentity=ObjectIdentity
syslogConformance=_SyslogConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,17,2))
_SyslogCompliances_ObjectIdentity=ObjectIdentity
syslogCompliances=_SyslogCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,17,2,1))
_SyslogGroups_ObjectIdentity=ObjectIdentity
syslogGroups=_SyslogGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,17,2,2))
syslogBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,17,2,2,1))
syslogBasicGroupVer1.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:syslogBasicGroupVer1.setStatus(_A)
syslogServerGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,17,2,2,2))
syslogServerGroupVer1.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:syslogServerGroupVer1.setStatus(_A)
syslogMsgCustomizationGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,17,2,2,50))
syslogMsgCustomizationGroupVer1.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:syslogMsgCustomizationGroupVer1.setStatus(_A)
syslogBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,17,2,1,1))
syslogBasicComplVer1.setObjects(*((_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:syslogBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusSyslog':ipAddressStatusSyslog,_Z:syslogConfigSource,_a:syslogHost,_b:syslogPort,'ipAddressConfigSyslog':ipAddressConfigSyslog,_c:syslogSelectConfigSource,'ipAddressConfigSyslogStatic':ipAddressConfigSyslogStatic,_d:syslogStaticHost,_e:syslogStaticPort,'ipAddressConfigSyslogDhcp':ipAddressConfigSyslogDhcp,_f:syslogDhcpSiteSpecificCode,'syslogMIB':syslogMIB,'syslogMIBObjects':syslogMIBObjects,_S:syslogMsgMaxSeverity,_T:syslogMsgLocalMaxSeverity,_U:syslogMsgLocalMaxNbr,'syslogLocalMsgTable':syslogLocalMsgTable,'syslogLocalMsgEntry':syslogLocalMsgEntry,_W:syslogMsgLocalSeverity,_V:syslogMsgLocalTime,_X:syslogMsgLocalModule,_Y:syslogMsgLocalMsg,'syslogMsgCustomization':syslogMsgCustomization,_g:syslogMsgDisplayMacAddress,_h:syslogMsgDisplayTime,_i:syslogMsgDisplayTimeFormat,_j:syslogMsgDisplayLocalHost,'syslogConformance':syslogConformance,'syslogCompliances':syslogCompliances,'syslogBasicComplVer1':syslogBasicComplVer1,'syslogGroups':syslogGroups,_k:syslogBasicGroupVer1,_l:syslogServerGroupVer1,_m:syslogMsgCustomizationGroupVer1})