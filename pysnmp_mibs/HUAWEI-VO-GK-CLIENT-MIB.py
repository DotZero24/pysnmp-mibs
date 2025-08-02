_G='obsolete'
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
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceGKClientMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,8))
if mibBuilder.loadTexts:hwVoiceGKClientMIB.setRevisions(('2004-04-08 13:45',))
_HwVoGKClientObjects_ObjectIdentity=ObjectIdentity
hwVoGKClientObjects=_HwVoGKClientObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,8,1))
class _HwVoRasOn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HwVoRasOn_Type.__name__=_C
_HwVoRasOn_Object=MibScalar
hwVoRasOn=_HwVoRasOn_Object((1,3,6,1,4,1,2011,5,25,1,8,1,1),_HwVoRasOn_Type())
hwVoRasOn.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoRasOn.setStatus(_B)
_HwVoH323InterfaceIndex_Type=Integer32
_HwVoH323InterfaceIndex_Object=MibScalar
hwVoH323InterfaceIndex=_HwVoH323InterfaceIndex_Object((1,3,6,1,4,1,2011,5,25,1,8,1,2),_HwVoH323InterfaceIndex_Type())
hwVoH323InterfaceIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323InterfaceIndex.setStatus(_G)
_HwVoGwIPAddress_Type=IpAddress
_HwVoGwIPAddress_Object=MibScalar
hwVoGwIPAddress=_HwVoGwIPAddress_Object((1,3,6,1,4,1,2011,5,25,1,8,1,3),_HwVoGwIPAddress_Type())
hwVoGwIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoGwIPAddress.setStatus(_B)
class _HwVoH323GWID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HwVoH323GWID_Type.__name__=_D
_HwVoH323GWID_Object=MibScalar
hwVoH323GWID=_HwVoH323GWID_Object((1,3,6,1,4,1,2011,5,25,1,8,1,4),_HwVoH323GWID_Type())
hwVoH323GWID.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GWID.setStatus(_B)
class _HwVoH323GWSupportMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonstandard-compatible',1),('huawei',2)))
_HwVoH323GWSupportMode_Type.__name__=_C
_HwVoH323GWSupportMode_Object=MibScalar
hwVoH323GWSupportMode=_HwVoH323GWSupportMode_Object((1,3,6,1,4,1,2011,5,25,1,8,1,5),_HwVoH323GWSupportMode_Type())
hwVoH323GWSupportMode.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GWSupportMode.setStatus(_G)
class _HwVoH323GWAreaID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,960))
_HwVoH323GWAreaID_Type.__name__=_D
_HwVoH323GWAreaID_Object=MibScalar
hwVoH323GWAreaID=_HwVoH323GWAreaID_Object((1,3,6,1,4,1,2011,5,25,1,8,1,6),_HwVoH323GWAreaID_Type())
hwVoH323GWAreaID.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GWAreaID.setStatus(_B)
class _HwVoH323GKID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HwVoH323GKID_Type.__name__=_D
_HwVoH323GKID_Object=MibScalar
hwVoH323GKID=_HwVoH323GKID_Object((1,3,6,1,4,1,2011,5,25,1,8,1,7),_HwVoH323GKID_Type())
hwVoH323GKID.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GKID.setStatus(_B)
_HwVoH323GKIPAddress_Type=IpAddress
_HwVoH323GKIPAddress_Object=MibScalar
hwVoH323GKIPAddress=_HwVoH323GKIPAddress_Object((1,3,6,1,4,1,2011,5,25,1,8,1,8),_HwVoH323GKIPAddress_Type())
hwVoH323GKIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GKIPAddress.setStatus(_B)
class _HwVoH323GKPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwVoH323GKPort_Type.__name__=_C
_HwVoH323GKPort_Object=MibScalar
hwVoH323GKPort=_HwVoH323GKPort_Object((1,3,6,1,4,1,2011,5,25,1,8,1,9),_HwVoH323GKPort_Type())
hwVoH323GKPort.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GKPort.setStatus(_B)
class _HwVoH323GK2ID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HwVoH323GK2ID_Type.__name__=_D
_HwVoH323GK2ID_Object=MibScalar
hwVoH323GK2ID=_HwVoH323GK2ID_Object((1,3,6,1,4,1,2011,5,25,1,8,1,10),_HwVoH323GK2ID_Type())
hwVoH323GK2ID.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GK2ID.setStatus(_B)
_HwVoH323GK2IPAddress_Type=IpAddress
_HwVoH323GK2IPAddress_Object=MibScalar
hwVoH323GK2IPAddress=_HwVoH323GK2IPAddress_Object((1,3,6,1,4,1,2011,5,25,1,8,1,11),_HwVoH323GK2IPAddress_Type())
hwVoH323GK2IPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GK2IPAddress.setStatus(_B)
class _HwVoH323GK2Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HwVoH323GK2Port_Type.__name__=_C
_HwVoH323GK2Port_Object=MibScalar
hwVoH323GK2Port=_HwVoH323GK2Port_Object((1,3,6,1,4,1,2011,5,25,1,8,1,12),_HwVoH323GK2Port_Type())
hwVoH323GK2Port.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GK2Port.setStatus(_B)
class _HwVoH323GKSecurityCall_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HwVoH323GKSecurityCall_Type.__name__=_C
_HwVoH323GKSecurityCall_Object=MibScalar
hwVoH323GKSecurityCall=_HwVoH323GKSecurityCall_Object((1,3,6,1,4,1,2011,5,25,1,8,1,13),_HwVoH323GKSecurityCall_Type())
hwVoH323GKSecurityCall.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GKSecurityCall.setStatus(_B)
class _HwVoH323GKSecurityPWDType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cipher',1),('simple',2)))
_HwVoH323GKSecurityPWDType_Type.__name__=_C
_HwVoH323GKSecurityPWDType_Object=MibScalar
hwVoH323GKSecurityPWDType=_HwVoH323GKSecurityPWDType_Object((1,3,6,1,4,1,2011,5,25,1,8,1,14),_HwVoH323GKSecurityPWDType_Type())
hwVoH323GKSecurityPWDType.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GKSecurityPWDType.setStatus(_B)
class _HwVoH323GKSecurityPWD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_HwVoH323GKSecurityPWD_Type.__name__=_D
_HwVoH323GKSecurityPWD_Object=MibScalar
hwVoH323GKSecurityPWD=_HwVoH323GKSecurityPWD_Object((1,3,6,1,4,1,2011,5,25,1,8,1,15),_HwVoH323GKSecurityPWD_Type())
hwVoH323GKSecurityPWD.setMaxAccess(_A)
if mibBuilder.loadTexts:hwVoH323GKSecurityPWD.setStatus(_B)
mibBuilder.exportSymbols('HUAWEI-VO-GK-CLIENT-MIB',**{'hwVoiceGKClientMIB':hwVoiceGKClientMIB,'hwVoGKClientObjects':hwVoGKClientObjects,'hwVoRasOn':hwVoRasOn,'hwVoH323InterfaceIndex':hwVoH323InterfaceIndex,'hwVoGwIPAddress':hwVoGwIPAddress,'hwVoH323GWID':hwVoH323GWID,'hwVoH323GWSupportMode':hwVoH323GWSupportMode,'hwVoH323GWAreaID':hwVoH323GWAreaID,'hwVoH323GKID':hwVoH323GKID,'hwVoH323GKIPAddress':hwVoH323GKIPAddress,'hwVoH323GKPort':hwVoH323GKPort,'hwVoH323GK2ID':hwVoH323GK2ID,'hwVoH323GK2IPAddress':hwVoH323GK2IPAddress,'hwVoH323GK2Port':hwVoH323GK2Port,'hwVoH323GKSecurityCall':hwVoH323GKSecurityCall,'hwVoH323GKSecurityPWDType':hwVoH323GKSecurityPWDType,'hwVoH323GKSecurityPWD':hwVoH323GKSecurityPWD})