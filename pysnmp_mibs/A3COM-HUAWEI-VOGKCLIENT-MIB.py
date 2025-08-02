_F='disable'
_E='enable'
_D='OctetString'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cVoice')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cVoiceGKClient=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,39,8))
if mibBuilder.loadTexts:h3cVoiceGKClient.setRevisions(('2005-03-15 00:00',))
_H3cVoGKClientObjects_ObjectIdentity=ObjectIdentity
h3cVoGKClientObjects=_H3cVoGKClientObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,8,1))
class _H3cVoRasOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_H3cVoRasOn_Type.__name__=_C
_H3cVoRasOn_Object=MibScalar
h3cVoRasOn=_H3cVoRasOn_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,1),_H3cVoRasOn_Type())
h3cVoRasOn.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoRasOn.setStatus(_B)
_H3cVoGwIPAddressType_Type=InetAddressType
_H3cVoGwIPAddressType_Object=MibScalar
h3cVoGwIPAddressType=_H3cVoGwIPAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,2),_H3cVoGwIPAddressType_Type())
h3cVoGwIPAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoGwIPAddressType.setStatus(_B)
_H3cVoGwIPAddress_Type=InetAddress
_H3cVoGwIPAddress_Object=MibScalar
h3cVoGwIPAddress=_H3cVoGwIPAddress_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,3),_H3cVoGwIPAddress_Type())
h3cVoGwIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoGwIPAddress.setStatus(_B)
class _H3cVoH323GWID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_H3cVoH323GWID_Type.__name__=_D
_H3cVoH323GWID_Object=MibScalar
h3cVoH323GWID=_H3cVoH323GWID_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,4),_H3cVoH323GWID_Type())
h3cVoH323GWID.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GWID.setStatus(_B)
class _H3cVoH323GKID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_H3cVoH323GKID_Type.__name__=_D
_H3cVoH323GKID_Object=MibScalar
h3cVoH323GKID=_H3cVoH323GKID_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,5),_H3cVoH323GKID_Type())
h3cVoH323GKID.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GKID.setStatus(_B)
_H3cVoH323GKIPAddressType_Type=InetAddressType
_H3cVoH323GKIPAddressType_Object=MibScalar
h3cVoH323GKIPAddressType=_H3cVoH323GKIPAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,6),_H3cVoH323GKIPAddressType_Type())
h3cVoH323GKIPAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GKIPAddressType.setStatus(_B)
_H3cVoH323GKIPAddress_Type=InetAddress
_H3cVoH323GKIPAddress_Object=MibScalar
h3cVoH323GKIPAddress=_H3cVoH323GKIPAddress_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,7),_H3cVoH323GKIPAddress_Type())
h3cVoH323GKIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GKIPAddress.setStatus(_B)
class _H3cVoH323GKPort_Type(Integer32):defaultValue=1719;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVoH323GKPort_Type.__name__=_C
_H3cVoH323GKPort_Object=MibScalar
h3cVoH323GKPort=_H3cVoH323GKPort_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,8),_H3cVoH323GKPort_Type())
h3cVoH323GKPort.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GKPort.setStatus(_B)
class _H3cVoH323GK2ID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_H3cVoH323GK2ID_Type.__name__=_D
_H3cVoH323GK2ID_Object=MibScalar
h3cVoH323GK2ID=_H3cVoH323GK2ID_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,9),_H3cVoH323GK2ID_Type())
h3cVoH323GK2ID.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GK2ID.setStatus(_B)
_H3cVoH323GK2IPAddressType_Type=InetAddressType
_H3cVoH323GK2IPAddressType_Object=MibScalar
h3cVoH323GK2IPAddressType=_H3cVoH323GK2IPAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,10),_H3cVoH323GK2IPAddressType_Type())
h3cVoH323GK2IPAddressType.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GK2IPAddressType.setStatus(_B)
_H3cVoH323GK2IPAddress_Type=InetAddress
_H3cVoH323GK2IPAddress_Object=MibScalar
h3cVoH323GK2IPAddress=_H3cVoH323GK2IPAddress_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,11),_H3cVoH323GK2IPAddress_Type())
h3cVoH323GK2IPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GK2IPAddress.setStatus(_B)
class _H3cVoH323GK2Port_Type(Integer32):defaultValue=1719;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cVoH323GK2Port_Type.__name__=_C
_H3cVoH323GK2Port_Object=MibScalar
h3cVoH323GK2Port=_H3cVoH323GK2Port_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,12),_H3cVoH323GK2Port_Type())
h3cVoH323GK2Port.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GK2Port.setStatus(_B)
class _H3cVoH323GKSecurityCall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_H3cVoH323GKSecurityCall_Type.__name__=_C
_H3cVoH323GKSecurityCall_Object=MibScalar
h3cVoH323GKSecurityCall=_H3cVoH323GKSecurityCall_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,13),_H3cVoH323GKSecurityCall_Type())
h3cVoH323GKSecurityCall.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GKSecurityCall.setStatus(_B)
class _H3cVoH323GKSecurityPWDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cipher',1),('simple',2)))
_H3cVoH323GKSecurityPWDType_Type.__name__=_C
_H3cVoH323GKSecurityPWDType_Object=MibScalar
h3cVoH323GKSecurityPWDType=_H3cVoH323GKSecurityPWDType_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,14),_H3cVoH323GKSecurityPWDType_Type())
h3cVoH323GKSecurityPWDType.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GKSecurityPWDType.setStatus(_B)
_H3cVoH323GKSecurityPWD_Type=OctetString
_H3cVoH323GKSecurityPWD_Object=MibScalar
h3cVoH323GKSecurityPWD=_H3cVoH323GKSecurityPWD_Object((1,3,6,1,4,1,43,45,1,10,2,39,8,1,15),_H3cVoH323GKSecurityPWD_Type())
h3cVoH323GKSecurityPWD.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cVoH323GKSecurityPWD.setStatus(_B)
mibBuilder.exportSymbols('A3COM-HUAWEI-VOGKCLIENT-MIB',**{'h3cVoiceGKClient':h3cVoiceGKClient,'h3cVoGKClientObjects':h3cVoGKClientObjects,'h3cVoRasOn':h3cVoRasOn,'h3cVoGwIPAddressType':h3cVoGwIPAddressType,'h3cVoGwIPAddress':h3cVoGwIPAddress,'h3cVoH323GWID':h3cVoH323GWID,'h3cVoH323GKID':h3cVoH323GKID,'h3cVoH323GKIPAddressType':h3cVoH323GKIPAddressType,'h3cVoH323GKIPAddress':h3cVoH323GKIPAddress,'h3cVoH323GKPort':h3cVoH323GKPort,'h3cVoH323GK2ID':h3cVoH323GK2ID,'h3cVoH323GK2IPAddressType':h3cVoH323GK2IPAddressType,'h3cVoH323GK2IPAddress':h3cVoH323GK2IPAddress,'h3cVoH323GK2Port':h3cVoH323GK2Port,'h3cVoH323GKSecurityCall':h3cVoH323GKSecurityCall,'h3cVoH323GKSecurityPWDType':h3cVoH323GKSecurityPWDType,'h3cVoH323GKSecurityPWD':h3cVoH323GKSecurityPWD})