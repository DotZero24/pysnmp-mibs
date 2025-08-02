_J='hwVoAAAGwAccessnumber'
_I='read-only'
_H='hwVoAAAClientLocalUserName'
_G='HUAWEI-VO-AAA-CLIENT-MIB'
_F='OctetString'
_E='disable'
_D='enable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceAAAClientMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,9))
if mibBuilder.loadTexts:hwVoiceAAAClientMIB.setRevisions(('2004-04-08 13:45',))
class EntryStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_HwVoAAAClientObjects_ObjectIdentity=ObjectIdentity
hwVoAAAClientObjects=_HwVoAAAClientObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,9,1))
_HwVoAAAClientCfgObjects_ObjectIdentity=ObjectIdentity
hwVoAAAClientCfgObjects=_HwVoAAAClientCfgObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,9,1,1))
class _HwVoAAAEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HwVoAAAEnable_Type.__name__=_C
_HwVoAAAEnable_Object=MibScalar
hwVoAAAEnable=_HwVoAAAEnable_Object((1,3,6,1,4,1,2011,5,25,1,9,1,1,1),_HwVoAAAEnable_Type())
hwVoAAAEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAEnable.setStatus(_A)
class _HwVoAAAClienttype_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('huawei',1),('nonstandard-compatible-vsa',2),('nonstandard-compatible-overload',3),('ietf-rfc',4)))
_HwVoAAAClienttype_Type.__name__=_C
_HwVoAAAClienttype_Object=MibScalar
hwVoAAAClienttype=_HwVoAAAClienttype_Object((1,3,6,1,4,1,2011,5,25,1,9,1,1,2),_HwVoAAAClienttype_Type())
hwVoAAAClienttype.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAClienttype.setStatus(_A)
class _HwVoAAAGwAuthenDidH323_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HwVoAAAGwAuthenDidH323_Type.__name__=_C
_HwVoAAAGwAuthenDidH323_Object=MibScalar
hwVoAAAGwAuthenDidH323=_HwVoAAAGwAuthenDidH323_Object((1,3,6,1,4,1,2011,5,25,1,9,1,1,3),_HwVoAAAGwAuthenDidH323_Type())
hwVoAAAGwAuthenDidH323.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwAuthenDidH323.setStatus(_A)
class _HwVoAAAGwAuthorDidH323_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HwVoAAAGwAuthorDidH323_Type.__name__=_C
_HwVoAAAGwAuthorDidH323_Object=MibScalar
hwVoAAAGwAuthorDidH323=_HwVoAAAGwAuthorDidH323_Object((1,3,6,1,4,1,2011,5,25,1,9,1,1,4),_HwVoAAAGwAuthorDidH323_Type())
hwVoAAAGwAuthorDidH323.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwAuthorDidH323.setStatus(_A)
class _HwVoAAAGwAccounting_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HwVoAAAGwAccounting_Type.__name__=_C
_HwVoAAAGwAccounting_Object=MibScalar
hwVoAAAGwAccounting=_HwVoAAAGwAccounting_Object((1,3,6,1,4,1,2011,5,25,1,9,1,1,5),_HwVoAAAGwAccounting_Type())
hwVoAAAGwAccounting.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwAccounting.setStatus(_A)
class _HwVoAAAGwAccountMethod_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('start-ack',2),('start-no-ack',3),('stop-only',4)))
_HwVoAAAGwAccountMethod_Type.__name__=_C
_HwVoAAAGwAccountMethod_Object=MibScalar
hwVoAAAGwAccountMethod=_HwVoAAAGwAccountMethod_Object((1,3,6,1,4,1,2011,5,25,1,9,1,1,6),_HwVoAAAGwAccountMethod_Type())
hwVoAAAGwAccountMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwAccountMethod.setStatus(_A)
_HwVoAAAClientLocalUserTable_Object=MibTable
hwVoAAAClientLocalUserTable=_HwVoAAAClientLocalUserTable_Object((1,3,6,1,4,1,2011,5,25,1,9,1,2))
if mibBuilder.loadTexts:hwVoAAAClientLocalUserTable.setStatus(_A)
_HwVoAAAClientLocalUserEntry_Object=MibTableRow
hwVoAAAClientLocalUserEntry=_HwVoAAAClientLocalUserEntry_Object((1,3,6,1,4,1,2011,5,25,1,9,1,2,1))
hwVoAAAClientLocalUserEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hwVoAAAClientLocalUserEntry.setStatus(_A)
class _HwVoAAAClientLocalUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_HwVoAAAClientLocalUserName_Type.__name__=_F
_HwVoAAAClientLocalUserName_Object=MibTableColumn
hwVoAAAClientLocalUserName=_HwVoAAAClientLocalUserName_Object((1,3,6,1,4,1,2011,5,25,1,9,1,2,1,1),_HwVoAAAClientLocalUserName_Type())
hwVoAAAClientLocalUserName.setMaxAccess(_I)
if mibBuilder.loadTexts:hwVoAAAClientLocalUserName.setStatus(_A)
class _HwVoAAAClientLocalUserPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HwVoAAAClientLocalUserPassword_Type.__name__=_F
_HwVoAAAClientLocalUserPassword_Object=MibTableColumn
hwVoAAAClientLocalUserPassword=_HwVoAAAClientLocalUserPassword_Object((1,3,6,1,4,1,2011,5,25,1,9,1,2,1,2),_HwVoAAAClientLocalUserPassword_Type())
hwVoAAAClientLocalUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAClientLocalUserPassword.setStatus(_A)
_HwVoAAAClientLocalRowStatus_Type=EntryStatus
_HwVoAAAClientLocalRowStatus_Object=MibTableColumn
hwVoAAAClientLocalRowStatus=_HwVoAAAClientLocalRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,9,1,2,1,3),_HwVoAAAClientLocalRowStatus_Type())
hwVoAAAClientLocalRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAClientLocalRowStatus.setStatus(_A)
_HwVoAAAGwAccessNumberTable_Object=MibTable
hwVoAAAGwAccessNumberTable=_HwVoAAAGwAccessNumberTable_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3))
if mibBuilder.loadTexts:hwVoAAAGwAccessNumberTable.setStatus(_A)
_HwVoAAAGwAccessNumberEntry_Object=MibTableRow
hwVoAAAGwAccessNumberEntry=_HwVoAAAGwAccessNumberEntry_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1))
hwVoAAAGwAccessNumberEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:hwVoAAAGwAccessNumberEntry.setStatus(_A)
class _HwVoAAAGwAccessnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwVoAAAGwAccessnumber_Type.__name__=_F
_HwVoAAAGwAccessnumber_Object=MibTableColumn
hwVoAAAGwAccessnumber=_HwVoAAAGwAccessnumber_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,1),_HwVoAAAGwAccessnumber_Type())
hwVoAAAGwAccessnumber.setMaxAccess(_I)
if mibBuilder.loadTexts:hwVoAAAGwAccessnumber.setStatus(_A)
class _HwVoAAAGwAuthentication_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HwVoAAAGwAuthentication_Type.__name__=_C
_HwVoAAAGwAuthentication_Object=MibTableColumn
hwVoAAAGwAuthentication=_HwVoAAAGwAuthentication_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,2),_HwVoAAAGwAuthentication_Type())
hwVoAAAGwAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwAuthentication.setStatus(_A)
class _HwVoAAAGwAuthorization_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HwVoAAAGwAuthorization_Type.__name__=_C
_HwVoAAAGwAuthorization_Object=MibTableColumn
hwVoAAAGwAuthorization=_HwVoAAAGwAuthorization_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,3),_HwVoAAAGwAuthorization_Type())
hwVoAAAGwAuthorization.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwAuthorization.setStatus(_A)
class _HwVoAAAGwProcessConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('callernumber',1),('cardnumber',2)))
_HwVoAAAGwProcessConfig_Type.__name__=_C
_HwVoAAAGwProcessConfig_Object=MibTableColumn
hwVoAAAGwProcessConfig=_HwVoAAAGwProcessConfig_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,4),_HwVoAAAGwProcessConfig_Type())
hwVoAAAGwProcessConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwProcessConfig.setStatus(_A)
class _HwVoAAAGwCardDigit_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_HwVoAAAGwCardDigit_Type.__name__=_C
_HwVoAAAGwCardDigit_Object=MibTableColumn
hwVoAAAGwCardDigit=_HwVoAAAGwCardDigit_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,5),_HwVoAAAGwCardDigit_Type())
hwVoAAAGwCardDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwCardDigit.setStatus(_A)
class _HwVoAAAGwPasswordDigit_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoAAAGwPasswordDigit_Type.__name__=_C
_HwVoAAAGwPasswordDigit_Object=MibTableColumn
hwVoAAAGwPasswordDigit=_HwVoAAAGwPasswordDigit_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,6),_HwVoAAAGwPasswordDigit_Type())
hwVoAAAGwPasswordDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwPasswordDigit.setStatus(_A)
class _HwVoAAAGwRedialtimes_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HwVoAAAGwRedialtimes_Type.__name__=_C
_HwVoAAAGwRedialtimes_Object=MibTableColumn
hwVoAAAGwRedialtimes=_HwVoAAAGwRedialtimes_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,7),_HwVoAAAGwRedialtimes_Type())
hwVoAAAGwRedialtimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwRedialtimes.setStatus(_A)
_HwVoAAAGwRowStatus_Type=EntryStatus
_HwVoAAAGwRowStatus_Object=MibTableColumn
hwVoAAAGwRowStatus=_HwVoAAAGwRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,9,1,3,1,8),_HwVoAAAGwRowStatus_Type())
hwVoAAAGwRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoAAAGwRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'EntryStatus':EntryStatus,'hwVoiceAAAClientMIB':hwVoiceAAAClientMIB,'hwVoAAAClientObjects':hwVoAAAClientObjects,'hwVoAAAClientCfgObjects':hwVoAAAClientCfgObjects,'hwVoAAAEnable':hwVoAAAEnable,'hwVoAAAClienttype':hwVoAAAClienttype,'hwVoAAAGwAuthenDidH323':hwVoAAAGwAuthenDidH323,'hwVoAAAGwAuthorDidH323':hwVoAAAGwAuthorDidH323,'hwVoAAAGwAccounting':hwVoAAAGwAccounting,'hwVoAAAGwAccountMethod':hwVoAAAGwAccountMethod,'hwVoAAAClientLocalUserTable':hwVoAAAClientLocalUserTable,'hwVoAAAClientLocalUserEntry':hwVoAAAClientLocalUserEntry,_H:hwVoAAAClientLocalUserName,'hwVoAAAClientLocalUserPassword':hwVoAAAClientLocalUserPassword,'hwVoAAAClientLocalRowStatus':hwVoAAAClientLocalRowStatus,'hwVoAAAGwAccessNumberTable':hwVoAAAGwAccessNumberTable,'hwVoAAAGwAccessNumberEntry':hwVoAAAGwAccessNumberEntry,_J:hwVoAAAGwAccessnumber,'hwVoAAAGwAuthentication':hwVoAAAGwAuthentication,'hwVoAAAGwAuthorization':hwVoAAAGwAuthorization,'hwVoAAAGwProcessConfig':hwVoAAAGwProcessConfig,'hwVoAAAGwCardDigit':hwVoAAAGwCardDigit,'hwVoAAAGwPasswordDigit':hwVoAAAGwPasswordDigit,'hwVoAAAGwRedialtimes':hwVoAAAGwRedialtimes,'hwVoAAAGwRowStatus':hwVoAAAGwRowStatus})