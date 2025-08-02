_N='adGenAOSDnsNotificationGroup'
_M='adGenAOSDnsInfoGroup'
_L='adDnsIndividualResolutionFailure'
_K='sysName'
_J='SNMPv2-MIB'
_I='adDnsResourceRecordType'
_H='adDnsDomainName'
_G='adDnsRequestErrorCondition'
_F='adDnsNameserverInetAddress'
_E='adDnsNameserverInetAddressType'
_D='adDnsTimestamp'
_C='accessible-for-notify'
_B='current'
_A='ADTRAN-AOS-DNS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSApplications,adGenAOSConformance=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSApplications','adGenAOSConformance')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSDns=ModuleIdentity((1,3,6,1,4,1,664,5,53,8,1))
if mibBuilder.loadTexts:adGenAOSDns.setRevisions(('2012-04-30 00:00',))
class AdDnsRequestErrorConditionTC(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('noError',0),('formatError',1),('serverFailure',2),('nameError',3),('notImplemented',4),('refused',5),('unsuportedRCode',16),('malformedResponse',17),('parseError',18),('timeoutWaitingForResponse',19),('emptyResponse',20),('unsupportedType',21),('onlyRootAnswer',22),('portDeficiency',23),('noServerCOnfigured',24),('udpSendError',25)))
class AdDnsResourceRecordTypeTC(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,33,65537)));namedValues=NamedValues(*(('a',1),('ns',2),('md',3),('mf',4),('cname',5),('soa',6),('mb',7),('mg',8),('mr',9),('null',10),('wks',11),('ptr',12),('hinfo',13),('minfo',14),('mx',15),('txt',16),('aaaa',28),('srv',33),('aplusaaaa',65537)))
_AdDnsTraps_ObjectIdentity=ObjectIdentity
adDnsTraps=_AdDnsTraps_ObjectIdentity((1,3,6,1,4,1,664,5,53,8,1,0))
_AdDnsTimestamp_Type=Unsigned32
_AdDnsTimestamp_Object=MibScalar
adDnsTimestamp=_AdDnsTimestamp_Object((1,3,6,1,4,1,664,5,53,8,1,1),_AdDnsTimestamp_Type())
adDnsTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:adDnsTimestamp.setStatus(_B)
_AdDnsNameserverInetAddressType_Type=InetAddressType
_AdDnsNameserverInetAddressType_Object=MibScalar
adDnsNameserverInetAddressType=_AdDnsNameserverInetAddressType_Object((1,3,6,1,4,1,664,5,53,8,1,2),_AdDnsNameserverInetAddressType_Type())
adDnsNameserverInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:adDnsNameserverInetAddressType.setStatus(_B)
_AdDnsNameserverInetAddress_Type=InetAddress
_AdDnsNameserverInetAddress_Object=MibScalar
adDnsNameserverInetAddress=_AdDnsNameserverInetAddress_Object((1,3,6,1,4,1,664,5,53,8,1,3),_AdDnsNameserverInetAddress_Type())
adDnsNameserverInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adDnsNameserverInetAddress.setStatus(_B)
_AdDnsRequestErrorCondition_Type=AdDnsRequestErrorConditionTC
_AdDnsRequestErrorCondition_Object=MibScalar
adDnsRequestErrorCondition=_AdDnsRequestErrorCondition_Object((1,3,6,1,4,1,664,5,53,8,1,4),_AdDnsRequestErrorCondition_Type())
adDnsRequestErrorCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:adDnsRequestErrorCondition.setStatus(_B)
_AdDnsDomainName_Type=DisplayString
_AdDnsDomainName_Object=MibScalar
adDnsDomainName=_AdDnsDomainName_Object((1,3,6,1,4,1,664,5,53,8,1,5),_AdDnsDomainName_Type())
adDnsDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:adDnsDomainName.setStatus(_B)
_AdDnsResourceRecordType_Type=AdDnsResourceRecordTypeTC
_AdDnsResourceRecordType_Object=MibScalar
adDnsResourceRecordType=_AdDnsResourceRecordType_Object((1,3,6,1,4,1,664,5,53,8,1,6),_AdDnsResourceRecordType_Type())
adDnsResourceRecordType.setMaxAccess(_C)
if mibBuilder.loadTexts:adDnsResourceRecordType.setStatus(_B)
_AdGenAOSDnsConformance_ObjectIdentity=ObjectIdentity
adGenAOSDnsConformance=_AdGenAOSDnsConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,13))
_AdGenAOSDnsGroup_ObjectIdentity=ObjectIdentity
adGenAOSDnsGroup=_AdGenAOSDnsGroup_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,13,1))
_AdGenAOSDnsCompliances_ObjectIdentity=ObjectIdentity
adGenAOSDnsCompliances=_AdGenAOSDnsCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,13,2))
adGenAOSDnsInfoGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,13,1,1))
adGenAOSDnsInfoGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:adGenAOSDnsInfoGroup.setStatus(_B)
adDnsIndividualResolutionFailure=NotificationType((1,3,6,1,4,1,664,5,53,8,1,0,1))
adDnsIndividualResolutionFailure.setObjects(*((_J,_K),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:adDnsIndividualResolutionFailure.setStatus(_B)
adGenAOSDnsNotificationGroup=NotificationGroup((1,3,6,1,4,1,664,5,53,99,13,1,2))
adGenAOSDnsNotificationGroup.setObjects((_A,_L))
if mibBuilder.loadTexts:adGenAOSDnsNotificationGroup.setStatus(_B)
adGenAOSDnsFullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,13,2,1))
adGenAOSDnsFullCompliance.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:adGenAOSDnsFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AdDnsRequestErrorConditionTC':AdDnsRequestErrorConditionTC,'AdDnsResourceRecordTypeTC':AdDnsResourceRecordTypeTC,'adGenAOSDns':adGenAOSDns,'adDnsTraps':adDnsTraps,_L:adDnsIndividualResolutionFailure,_D:adDnsTimestamp,_E:adDnsNameserverInetAddressType,_F:adDnsNameserverInetAddress,_G:adDnsRequestErrorCondition,_H:adDnsDomainName,_I:adDnsResourceRecordType,'adGenAOSDnsConformance':adGenAOSDnsConformance,'adGenAOSDnsGroup':adGenAOSDnsGroup,_M:adGenAOSDnsInfoGroup,_N:adGenAOSDnsNotificationGroup,'adGenAOSDnsCompliances':adGenAOSDnsCompliances,'adGenAOSDnsFullCompliance':adGenAOSDnsFullCompliance})