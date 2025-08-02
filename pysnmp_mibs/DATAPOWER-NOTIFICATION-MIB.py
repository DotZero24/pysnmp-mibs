_L='dpNotificationObjectName'
_K='dpNotificationObject'
_J='dpNotificationDomain'
_I='dpNotificationText'
_H='dpNotificationTransId'
_G='dpNotificationTime'
_F='dpNotificationSeverity'
_E='dpNotificationType'
_D='Integer32'
_C='accessible-for-notify'
_B='current'
_A='DATAPOWER-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dpNotificationMIB=ModuleIdentity((1,3,6,1,4,1,14685,2,3))
if mibBuilder.loadTexts:dpNotificationMIB.setRevisions(('2007-01-11 00:00',))
_Datapower_ObjectIdentity=ObjectIdentity
datapower=_Datapower_ObjectIdentity((1,3,6,1,4,1,14685))
_DpModules_ObjectIdentity=ObjectIdentity
dpModules=_DpModules_ObjectIdentity((1,3,6,1,4,1,14685,2))
_DpManagement_ObjectIdentity=ObjectIdentity
dpManagement=_DpManagement_ObjectIdentity((1,3,6,1,4,1,14685,3))
_DpNotifications_ObjectIdentity=ObjectIdentity
dpNotifications=_DpNotifications_ObjectIdentity((1,3,6,1,4,1,14685,3,3))
_DpNotificationElements_ObjectIdentity=ObjectIdentity
dpNotificationElements=_DpNotificationElements_ObjectIdentity((1,3,6,1,4,1,14685,3,3,1))
class _DpNotificationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,283,284,285,286,287,288,289,290,291,292)));namedValues=NamedValues(*(('all',3),('aaa',4),('auth',5),('cli',6),('crypto',7),('file',8),('file-capture',9),('http',10),('ldap',11),('mgmt',12),('mime',13),('monitor',14),('mq',15),('multistep',16),('network',17),('ssl',18),('schema',19),('smtp',20),('system',21),('tam',22),('user',23),('useragent',24),('xslcoproc',25),('xmlfilter',26),('xmlfirewall',27),('xslt',28),('xsltmsg',29),('xmlparse',30),('xslproxy',31),('xmlroute',32),('cert-monitor',33),('ocsp',34),('ftp',68),('ws-proxy',69),('wsm-agent',70),('mpgw',71),('kerberos',72),('slm',73),('sql',74),('network-file',76),('icap',77),('webapp-firewall',78),('http-convert',79),('tibco-ems',80),('xacml',81),('ltpa',82),('latency',83),('wasjms',84),('file-poller',85),('tfim',86),('uddisub',87),('wsrr',88),('rbm',89),('rpcsec-gss',90),('secure-conversation',91),('ims',92),('iscsi',93),('audit',94),('wtx',95),('zosnss',96),('llm',97),('ssh',98),('sftp',99),('b2bgw',100),('b2bp',101),('cms',102),('uddi',246),('wcc',247),('self-balancing',248),('sysplexdistributor',249),('quiesce',250),('fibre-channel',251),('cluster-service',252),('secure-cloud-connector',253),('ipmi',254),('memory-report',255),('waxhn',256),('wag',257),('ip-multicast',258),('peer-group',259),('web-token-service',260),('oauth',261),('xc10-grid',262),('odr-connector-group',264),('odr',265),('odrlib',266),('gatewayscript',267),('gatewayscript-user',268),('extlatency',269),('cloud-gateway',270),('cloud-connector',271),('isamproxy',272),('wxs-grid',273),('sgclient',274),('apiconnect',275),('redis',276),('quota-enforcement',277),('networkhsm-luna',278),('dfdl',279),('xformng',280),('xquery',281),('parse',283),('tenant',284),('product-insights',285),('apigw',286),('apic-gw-service',287),('gateway-peering',288),('ilmt-scanner',289),('ilmt-force-scan',290),('gateway-peering-manager',291),('opentracing',292)))
_DpNotificationType_Type.__name__=_D
_DpNotificationType_Object=MibScalar
dpNotificationType=_DpNotificationType_Object((1,3,6,1,4,1,14685,3,3,1,1),_DpNotificationType_Type())
dpNotificationType.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationType.setStatus(_B)
class _DpNotificationSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emerg',1),('alert',2),('critic',3),('error',4),('warn',5),('notice',6),('info',7),('debug',8)))
_DpNotificationSeverity_Type.__name__=_D
_DpNotificationSeverity_Object=MibScalar
dpNotificationSeverity=_DpNotificationSeverity_Object((1,3,6,1,4,1,14685,3,3,1,2),_DpNotificationSeverity_Type())
dpNotificationSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationSeverity.setStatus(_B)
_DpNotificationTime_Type=DisplayString
_DpNotificationTime_Object=MibScalar
dpNotificationTime=_DpNotificationTime_Object((1,3,6,1,4,1,14685,3,3,1,3),_DpNotificationTime_Type())
dpNotificationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationTime.setStatus(_B)
_DpNotificationText_Type=DisplayString
_DpNotificationText_Object=MibScalar
dpNotificationText=_DpNotificationText_Object((1,3,6,1,4,1,14685,3,3,1,4),_DpNotificationText_Type())
dpNotificationText.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationText.setStatus(_B)
_DpNotificationObject_Type=ObjectIdentifier
_DpNotificationObject_Object=MibScalar
dpNotificationObject=_DpNotificationObject_Object((1,3,6,1,4,1,14685,3,3,1,5),_DpNotificationObject_Type())
dpNotificationObject.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationObject.setStatus(_B)
_DpNotificationObjectName_Type=DisplayString
_DpNotificationObjectName_Object=MibScalar
dpNotificationObjectName=_DpNotificationObjectName_Object((1,3,6,1,4,1,14685,3,3,1,6),_DpNotificationObjectName_Type())
dpNotificationObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationObjectName.setStatus(_B)
_DpNotificationTransId_Type=Unsigned32
_DpNotificationTransId_Object=MibScalar
dpNotificationTransId=_DpNotificationTransId_Object((1,3,6,1,4,1,14685,3,3,1,7),_DpNotificationTransId_Type())
dpNotificationTransId.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationTransId.setStatus(_B)
_DpNotificationDomain_Type=DisplayString
_DpNotificationDomain_Object=MibScalar
dpNotificationDomain=_DpNotificationDomain_Object((1,3,6,1,4,1,14685,3,3,1,8),_DpNotificationDomain_Type())
dpNotificationDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationDomain.setStatus(_B)
_DpNotificationEventCode_Type=DisplayString
_DpNotificationEventCode_Object=MibScalar
dpNotificationEventCode=_DpNotificationEventCode_Object((1,3,6,1,4,1,14685,3,3,1,9),_DpNotificationEventCode_Type())
dpNotificationEventCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dpNotificationEventCode.setStatus(_B)
_DpNotificationDefinitions_ObjectIdentity=ObjectIdentity
dpNotificationDefinitions=_DpNotificationDefinitions_ObjectIdentity((1,3,6,1,4,1,14685,3,3,2))
dpLogNotification=NotificationType((1,3,6,1,4,1,14685,3,3,2,0,1))
dpLogNotification.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:dpLogNotification.setStatus(_B)
dpLogInternalNotification=NotificationType((1,3,6,1,4,1,14685,3,3,2,0,2))
dpLogInternalNotification.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:dpLogInternalNotification.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'datapower':datapower,'dpModules':dpModules,'dpNotificationMIB':dpNotificationMIB,'dpManagement':dpManagement,'dpNotifications':dpNotifications,'dpNotificationElements':dpNotificationElements,_E:dpNotificationType,_F:dpNotificationSeverity,_G:dpNotificationTime,_I:dpNotificationText,_K:dpNotificationObject,_L:dpNotificationObjectName,_H:dpNotificationTransId,_J:dpNotificationDomain,'dpNotificationEventCode':dpNotificationEventCode,'dpNotificationDefinitions':dpNotificationDefinitions,'dpLogNotification':dpLogNotification,'dpLogInternalNotification':dpLogInternalNotification})