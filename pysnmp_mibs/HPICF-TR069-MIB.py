_Z='hpicfTR069Group'
_Y='hpicfTR069PeriodicInformTime'
_X='hpicfTR069PeriodicInformInterval'
_W='hpicfTR069PeriodicInformEnable'
_V='hpicfTR069CpeWaitTimeout'
_U='hpicfTR069CpePasswordEncrypted'
_T='hpicfTR069CpePassword'
_S='hpicfTR069CpeUsername'
_R='hpicfTR069AcsConnectRetryInterval'
_Q='hpicfTR069AcsPasswordEncrypted'
_P='hpicfTR069AcsPassword'
_O='hpicfTR069AcsUsername'
_N='hpicfTR069AcsProxyUrl'
_M='hpicfTR069AcsUrlOrigin'
_L='hpicfTR069AcsUrl'
_K='hpicfTR069CWMPDeviceType'
_J='hpicfTR069EnableCWMP'
_I='seconds'
_H='enable'
_G='disable'
_F='Integer32'
_E='read-only'
_D='OctetString'
_C='read-write'
_B='HPICF-TR069-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
hpicfTR069MIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,98))
if mibBuilder.loadTexts:hpicfTR069MIB.setRevisions(('2014-03-03 00:00',))
_HpicfTR069Notifications_ObjectIdentity=ObjectIdentity
hpicfTR069Notifications=_HpicfTR069Notifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,98,0))
_HpicfTR069Objects_ObjectIdentity=ObjectIdentity
hpicfTR069Objects=_HpicfTR069Objects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,98,1))
class _HpicfTR069EnableCWMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpicfTR069EnableCWMP_Type.__name__=_F
_HpicfTR069EnableCWMP_Object=MibScalar
hpicfTR069EnableCWMP=_HpicfTR069EnableCWMP_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,1),_HpicfTR069EnableCWMP_Type())
hpicfTR069EnableCWMP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069EnableCWMP.setStatus(_A)
class _HpicfTR069CWMPDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('device',1),('gateway',2)))
_HpicfTR069CWMPDeviceType_Type.__name__=_F
_HpicfTR069CWMPDeviceType_Object=MibScalar
hpicfTR069CWMPDeviceType=_HpicfTR069CWMPDeviceType_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,2),_HpicfTR069CWMPDeviceType_Type())
hpicfTR069CWMPDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069CWMPDeviceType.setStatus(_A)
class _HpicfTR069AcsUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfTR069AcsUrl_Type.__name__=_D
_HpicfTR069AcsUrl_Object=MibScalar
hpicfTR069AcsUrl=_HpicfTR069AcsUrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,3),_HpicfTR069AcsUrl_Type())
hpicfTR069AcsUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069AcsUrl.setStatus(_A)
class _HpicfTR069AcsUrlOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('config',2),('dhcp',3),('acs',4)))
_HpicfTR069AcsUrlOrigin_Type.__name__=_F
_HpicfTR069AcsUrlOrigin_Object=MibScalar
hpicfTR069AcsUrlOrigin=_HpicfTR069AcsUrlOrigin_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,4),_HpicfTR069AcsUrlOrigin_Type())
hpicfTR069AcsUrlOrigin.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTR069AcsUrlOrigin.setStatus(_A)
class _HpicfTR069AcsProxyUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfTR069AcsProxyUrl_Type.__name__=_D
_HpicfTR069AcsProxyUrl_Object=MibScalar
hpicfTR069AcsProxyUrl=_HpicfTR069AcsProxyUrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,5),_HpicfTR069AcsProxyUrl_Type())
hpicfTR069AcsProxyUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069AcsProxyUrl.setStatus(_A)
class _HpicfTR069AcsUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfTR069AcsUsername_Type.__name__=_D
_HpicfTR069AcsUsername_Object=MibScalar
hpicfTR069AcsUsername=_HpicfTR069AcsUsername_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,6),_HpicfTR069AcsUsername_Type())
hpicfTR069AcsUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069AcsUsername.setStatus(_A)
class _HpicfTR069AcsPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfTR069AcsPassword_Type.__name__=_D
_HpicfTR069AcsPassword_Object=MibScalar
hpicfTR069AcsPassword=_HpicfTR069AcsPassword_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,7),_HpicfTR069AcsPassword_Type())
hpicfTR069AcsPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069AcsPassword.setStatus(_A)
class _HpicfTR069AcsPasswordEncrypted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,384))
_HpicfTR069AcsPasswordEncrypted_Type.__name__=_D
_HpicfTR069AcsPasswordEncrypted_Object=MibScalar
hpicfTR069AcsPasswordEncrypted=_HpicfTR069AcsPasswordEncrypted_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,8),_HpicfTR069AcsPasswordEncrypted_Type())
hpicfTR069AcsPasswordEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069AcsPasswordEncrypted.setStatus(_A)
_HpicfTR069AcsConnectRetryInterval_Type=Unsigned32
_HpicfTR069AcsConnectRetryInterval_Object=MibScalar
hpicfTR069AcsConnectRetryInterval=_HpicfTR069AcsConnectRetryInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,9),_HpicfTR069AcsConnectRetryInterval_Type())
hpicfTR069AcsConnectRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTR069AcsConnectRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:hpicfTR069AcsConnectRetryInterval.setUnits(_I)
class _HpicfTR069CpeUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfTR069CpeUsername_Type.__name__=_D
_HpicfTR069CpeUsername_Object=MibScalar
hpicfTR069CpeUsername=_HpicfTR069CpeUsername_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,10),_HpicfTR069CpeUsername_Type())
hpicfTR069CpeUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069CpeUsername.setStatus(_A)
class _HpicfTR069CpePassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfTR069CpePassword_Type.__name__=_D
_HpicfTR069CpePassword_Object=MibScalar
hpicfTR069CpePassword=_HpicfTR069CpePassword_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,11),_HpicfTR069CpePassword_Type())
hpicfTR069CpePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069CpePassword.setStatus(_A)
class _HpicfTR069CpePasswordEncrypted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,384))
_HpicfTR069CpePasswordEncrypted_Type.__name__=_D
_HpicfTR069CpePasswordEncrypted_Object=MibScalar
hpicfTR069CpePasswordEncrypted=_HpicfTR069CpePasswordEncrypted_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,12),_HpicfTR069CpePasswordEncrypted_Type())
hpicfTR069CpePasswordEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTR069CpePasswordEncrypted.setStatus(_A)
_HpicfTR069CpeWaitTimeout_Type=Unsigned32
_HpicfTR069CpeWaitTimeout_Object=MibScalar
hpicfTR069CpeWaitTimeout=_HpicfTR069CpeWaitTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,13),_HpicfTR069CpeWaitTimeout_Type())
hpicfTR069CpeWaitTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTR069CpeWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpicfTR069CpeWaitTimeout.setUnits(_I)
class _HpicfTR069PeriodicInformEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpicfTR069PeriodicInformEnable_Type.__name__=_F
_HpicfTR069PeriodicInformEnable_Object=MibScalar
hpicfTR069PeriodicInformEnable=_HpicfTR069PeriodicInformEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,14),_HpicfTR069PeriodicInformEnable_Type())
hpicfTR069PeriodicInformEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTR069PeriodicInformEnable.setStatus(_A)
_HpicfTR069PeriodicInformInterval_Type=Unsigned32
_HpicfTR069PeriodicInformInterval_Object=MibScalar
hpicfTR069PeriodicInformInterval=_HpicfTR069PeriodicInformInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,15),_HpicfTR069PeriodicInformInterval_Type())
hpicfTR069PeriodicInformInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTR069PeriodicInformInterval.setStatus(_A)
_HpicfTR069PeriodicInformTime_Type=DateAndTime
_HpicfTR069PeriodicInformTime_Object=MibScalar
hpicfTR069PeriodicInformTime=_HpicfTR069PeriodicInformTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,98,1,16),_HpicfTR069PeriodicInformTime_Type())
hpicfTR069PeriodicInformTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTR069PeriodicInformTime.setStatus(_A)
_HpicfTR069Conformance_ObjectIdentity=ObjectIdentity
hpicfTR069Conformance=_HpicfTR069Conformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,98,2))
_HpicfTR069MIBCompliances_ObjectIdentity=ObjectIdentity
hpicfTR069MIBCompliances=_HpicfTR069MIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,98,2,1))
_HpicfTR069MIBGroups_ObjectIdentity=ObjectIdentity
hpicfTR069MIBGroups=_HpicfTR069MIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,98,2,2))
hpicfTR069Group=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,98,2,2,1))
hpicfTR069Group.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hpicfTR069Group.setStatus(_A)
hpicfTR069MIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,98,2,1,1))
hpicfTR069MIBCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:hpicfTR069MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfTR069MIB':hpicfTR069MIB,'hpicfTR069Notifications':hpicfTR069Notifications,'hpicfTR069Objects':hpicfTR069Objects,_J:hpicfTR069EnableCWMP,_K:hpicfTR069CWMPDeviceType,_L:hpicfTR069AcsUrl,_M:hpicfTR069AcsUrlOrigin,_N:hpicfTR069AcsProxyUrl,_O:hpicfTR069AcsUsername,_P:hpicfTR069AcsPassword,_Q:hpicfTR069AcsPasswordEncrypted,_R:hpicfTR069AcsConnectRetryInterval,_S:hpicfTR069CpeUsername,_T:hpicfTR069CpePassword,_U:hpicfTR069CpePasswordEncrypted,_V:hpicfTR069CpeWaitTimeout,_W:hpicfTR069PeriodicInformEnable,_X:hpicfTR069PeriodicInformInterval,_Y:hpicfTR069PeriodicInformTime,'hpicfTR069Conformance':hpicfTR069Conformance,'hpicfTR069MIBCompliances':hpicfTR069MIBCompliances,'hpicfTR069MIBCompliance':hpicfTR069MIBCompliance,'hpicfTR069MIBGroups':hpicfTR069MIBGroups,_Z:hpicfTR069Group})