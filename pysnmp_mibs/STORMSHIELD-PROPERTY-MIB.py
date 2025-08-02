_C='DisplayString'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsProductProperty=ModuleIdentity((1,3,6,1,4,1,11256,1,0))
if mibBuilder.loadTexts:snsProductProperty.setRevisions(('2017-02-20 00:00',))
class _SnsModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsModel_Type.__name__=_C
_SnsModel_Object=MibScalar
snsModel=_SnsModel_Object((1,3,6,1,4,1,11256,1,0,1),_SnsModel_Type())
snsModel.setMaxAccess(_A)
if mibBuilder.loadTexts:snsModel.setStatus(_B)
class _SnsVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsVersion_Type.__name__=_C
_SnsVersion_Object=MibScalar
snsVersion=_SnsVersion_Object((1,3,6,1,4,1,11256,1,0,2),_SnsVersion_Type())
snsVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:snsVersion.setStatus(_B)
class _SnsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsSerialNumber_Type.__name__=_C
_SnsSerialNumber_Object=MibScalar
snsSerialNumber=_SnsSerialNumber_Object((1,3,6,1,4,1,11256,1,0,3),_SnsSerialNumber_Type())
snsSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:snsSerialNumber.setStatus(_B)
class _SnsSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsSystemName_Type.__name__=_C
_SnsSystemName_Object=MibScalar
snsSystemName=_SnsSystemName_Object((1,3,6,1,4,1,11256,1,0,4),_SnsSystemName_Type())
snsSystemName.setMaxAccess(_A)
if mibBuilder.loadTexts:snsSystemName.setStatus(_B)
class _SnsSystemLanguage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsSystemLanguage_Type.__name__=_C
_SnsSystemLanguage_Object=MibScalar
snsSystemLanguage=_SnsSystemLanguage_Object((1,3,6,1,4,1,11256,1,0,5),_SnsSystemLanguage_Type())
snsSystemLanguage.setMaxAccess(_A)
if mibBuilder.loadTexts:snsSystemLanguage.setStatus(_B)
_SnsNbEther_Type=Integer32
_SnsNbEther_Object=MibScalar
snsNbEther=_SnsNbEther_Object((1,3,6,1,4,1,11256,1,0,6),_SnsNbEther_Type())
snsNbEther.setMaxAccess(_A)
if mibBuilder.loadTexts:snsNbEther.setStatus(_B)
_SnsNbVlan_Type=Integer32
_SnsNbVlan_Object=MibScalar
snsNbVlan=_SnsNbVlan_Object((1,3,6,1,4,1,11256,1,0,7),_SnsNbVlan_Type())
snsNbVlan.setMaxAccess(_A)
if mibBuilder.loadTexts:snsNbVlan.setStatus(_B)
_SnsNbDialup_Type=Integer32
_SnsNbDialup_Object=MibScalar
snsNbDialup=_SnsNbDialup_Object((1,3,6,1,4,1,11256,1,0,8),_SnsNbDialup_Type())
snsNbDialup.setMaxAccess(_A)
if mibBuilder.loadTexts:snsNbDialup.setStatus(_B)
_SnsNbPPTP_Type=Integer32
_SnsNbPPTP_Object=MibScalar
snsNbPPTP=_SnsNbPPTP_Object((1,3,6,1,4,1,11256,1,0,9),_SnsNbPPTP_Type())
snsNbPPTP.setMaxAccess(_A)
if mibBuilder.loadTexts:snsNbPPTP.setStatus(_B)
_SnsNbSerial_Type=Integer32
_SnsNbSerial_Object=MibScalar
snsNbSerial=_SnsNbSerial_Object((1,3,6,1,4,1,11256,1,0,10),_SnsNbSerial_Type())
snsNbSerial.setMaxAccess(_A)
if mibBuilder.loadTexts:snsNbSerial.setStatus(_B)
_SnsNbLoopback_Type=Integer32
_SnsNbLoopback_Object=MibScalar
snsNbLoopback=_SnsNbLoopback_Object((1,3,6,1,4,1,11256,1,0,11),_SnsNbLoopback_Type())
snsNbLoopback.setMaxAccess(_A)
if mibBuilder.loadTexts:snsNbLoopback.setStatus(_B)
_SnsWatchdog_Type=Integer32
_SnsWatchdog_Object=MibScalar
snsWatchdog=_SnsWatchdog_Object((1,3,6,1,4,1,11256,1,0,12),_SnsWatchdog_Type())
snsWatchdog.setMaxAccess(_A)
if mibBuilder.loadTexts:snsWatchdog.setStatus(_B)
_SnsLed_Type=Integer32
_SnsLed_Object=MibScalar
snsLed=_SnsLed_Object((1,3,6,1,4,1,11256,1,0,13),_SnsLed_Type())
snsLed.setMaxAccess(_A)
if mibBuilder.loadTexts:snsLed.setStatus(_B)
_SnsClone_Type=Integer32
_SnsClone_Object=MibScalar
snsClone=_SnsClone_Object((1,3,6,1,4,1,11256,1,0,14),_SnsClone_Type())
snsClone.setMaxAccess(_A)
if mibBuilder.loadTexts:snsClone.setStatus(_B)
_SnsHADialup_Type=Integer32
_SnsHADialup_Object=MibScalar
snsHADialup=_SnsHADialup_Object((1,3,6,1,4,1,11256,1,0,15),_SnsHADialup_Type())
snsHADialup.setMaxAccess(_A)
if mibBuilder.loadTexts:snsHADialup.setStatus(_B)
mibBuilder.exportSymbols('STORMSHIELD-PROPERTY-MIB',**{'snsProductProperty':snsProductProperty,'snsModel':snsModel,'snsVersion':snsVersion,'snsSerialNumber':snsSerialNumber,'snsSystemName':snsSystemName,'snsSystemLanguage':snsSystemLanguage,'snsNbEther':snsNbEther,'snsNbVlan':snsNbVlan,'snsNbDialup':snsNbDialup,'snsNbPPTP':snsNbPPTP,'snsNbSerial':snsNbSerial,'snsNbLoopback':snsNbLoopback,'snsWatchdog':snsWatchdog,'snsLed':snsLed,'snsClone':snsClone,'snsHADialup':snsHADialup})