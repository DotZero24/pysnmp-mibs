_E='DisplayString'
_D='read-only'
_C='jnxWxCommonEventDescr'
_B='JUNIPER-WX-COMMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxWxCommonMib,jnxWxModules=mibBuilder.importSymbols('JUNIPER-WX-GLOBAL-REG','jnxWxCommonMib','jnxWxModules')
TcChassisType,=mibBuilder.importSymbols('JUNIPER-WX-GLOBAL-TC','TcChassisType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TruthValue')
jnxWxCommonMibModule=ModuleIdentity((1,3,6,1,4,1,8239,1,1,3))
if mibBuilder.loadTexts:jnxWxCommonMibModule.setRevisions(('2003-09-30 08:45','2003-04-01 00:00','2003-03-10 00:00','2002-06-03 00:00','2002-03-27 00:00','2002-02-22 00:00','2002-01-23 00:00','2002-01-17 00:00','2001-08-07 00:00'))
_JnxWxCommonConfMib_ObjectIdentity=ObjectIdentity
jnxWxCommonConfMib=_JnxWxCommonConfMib_ObjectIdentity((1,3,6,1,4,1,8239,2,1,1))
if mibBuilder.loadTexts:jnxWxCommonConfMib.setStatus(_A)
_JnxWxCommonObjs_ObjectIdentity=ObjectIdentity
jnxWxCommonObjs=_JnxWxCommonObjs_ObjectIdentity((1,3,6,1,4,1,8239,2,1,2))
if mibBuilder.loadTexts:jnxWxCommonObjs.setStatus(_A)
_JnxWxSys_ObjectIdentity=ObjectIdentity
jnxWxSys=_JnxWxSys_ObjectIdentity((1,3,6,1,4,1,8239,2,1,2,1))
if mibBuilder.loadTexts:jnxWxSys.setStatus(_A)
class _JnxWxSysSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JnxWxSysSwVersion_Type.__name__=_E
_JnxWxSysSwVersion_Object=MibScalar
jnxWxSysSwVersion=_JnxWxSysSwVersion_Object((1,3,6,1,4,1,8239,2,1,2,1,1),_JnxWxSysSwVersion_Type())
jnxWxSysSwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxWxSysSwVersion.setStatus(_A)
class _JnxWxSysHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JnxWxSysHwVersion_Type.__name__=_E
_JnxWxSysHwVersion_Object=MibScalar
jnxWxSysHwVersion=_JnxWxSysHwVersion_Object((1,3,6,1,4,1,8239,2,1,2,1,2),_JnxWxSysHwVersion_Type())
jnxWxSysHwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxWxSysHwVersion.setStatus(_A)
class _JnxWxSysSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_JnxWxSysSerialNumber_Type.__name__=_E
_JnxWxSysSerialNumber_Object=MibScalar
jnxWxSysSerialNumber=_JnxWxSysSerialNumber_Object((1,3,6,1,4,1,8239,2,1,2,1,3),_JnxWxSysSerialNumber_Type())
jnxWxSysSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxWxSysSerialNumber.setStatus(_A)
_JnxWxSysTimeZoneOffset_Type=Integer32
_JnxWxSysTimeZoneOffset_Object=MibScalar
jnxWxSysTimeZoneOffset=_JnxWxSysTimeZoneOffset_Object((1,3,6,1,4,1,8239,2,1,2,1,4),_JnxWxSysTimeZoneOffset_Type())
jnxWxSysTimeZoneOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxWxSysTimeZoneOffset.setStatus(_A)
_JnxWxSysDaylightSaving_Type=TruthValue
_JnxWxSysDaylightSaving_Object=MibScalar
jnxWxSysDaylightSaving=_JnxWxSysDaylightSaving_Object((1,3,6,1,4,1,8239,2,1,2,1,5),_JnxWxSysDaylightSaving_Type())
jnxWxSysDaylightSaving.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxWxSysDaylightSaving.setStatus(_A)
_JnxWxChassis_ObjectIdentity=ObjectIdentity
jnxWxChassis=_JnxWxChassis_ObjectIdentity((1,3,6,1,4,1,8239,2,1,2,2))
if mibBuilder.loadTexts:jnxWxChassis.setStatus(_A)
_JnxWxChassisType_Type=TcChassisType
_JnxWxChassisType_Object=MibScalar
jnxWxChassisType=_JnxWxChassisType_Object((1,3,6,1,4,1,8239,2,1,2,2,1),_JnxWxChassisType_Type())
jnxWxChassisType.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxWxChassisType.setStatus(_A)
_JnxWxCommonEvents_ObjectIdentity=ObjectIdentity
jnxWxCommonEvents=_JnxWxCommonEvents_ObjectIdentity((1,3,6,1,4,1,8239,2,1,3))
if mibBuilder.loadTexts:jnxWxCommonEvents.setStatus(_A)
_JnxWxCommonEventObjs_ObjectIdentity=ObjectIdentity
jnxWxCommonEventObjs=_JnxWxCommonEventObjs_ObjectIdentity((1,3,6,1,4,1,8239,2,1,3,1))
if mibBuilder.loadTexts:jnxWxCommonEventObjs.setStatus(_A)
_JnxWxCommonEventDescr_Type=DisplayString
_JnxWxCommonEventDescr_Object=MibScalar
jnxWxCommonEventDescr=_JnxWxCommonEventDescr_Object((1,3,6,1,4,1,8239,2,1,3,1,1),_JnxWxCommonEventDescr_Type())
jnxWxCommonEventDescr.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:jnxWxCommonEventDescr.setStatus(_A)
_JnxWxCommonEventEvents_ObjectIdentity=ObjectIdentity
jnxWxCommonEventEvents=_JnxWxCommonEventEvents_ObjectIdentity((1,3,6,1,4,1,8239,2,1,3,2))
if mibBuilder.loadTexts:jnxWxCommonEventEvents.setStatus(_A)
_JnxWxCommonEventEventsV2_ObjectIdentity=ObjectIdentity
jnxWxCommonEventEventsV2=_JnxWxCommonEventEventsV2_ObjectIdentity((1,3,6,1,4,1,8239,2,1,3,2,0))
if mibBuilder.loadTexts:jnxWxCommonEventEventsV2.setStatus(_A)
jnxWxCommonEventInFailSafeMode=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,1))
if mibBuilder.loadTexts:jnxWxCommonEventInFailSafeMode.setStatus(_A)
jnxWxCommonEventPowerSupplyFailure=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,2))
if mibBuilder.loadTexts:jnxWxCommonEventPowerSupplyFailure.setStatus(_A)
jnxWxCommonEventPowerSupplyOk=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,3))
if mibBuilder.loadTexts:jnxWxCommonEventPowerSupplyOk.setStatus(_A)
jnxWxCommonEventLicenseExpired=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,4))
jnxWxCommonEventLicenseExpired.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventLicenseExpired.setStatus(_A)
jnxWxCommonEventThruputLimitExceeded=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,5))
jnxWxCommonEventThruputLimitExceeded.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventThruputLimitExceeded.setStatus(_A)
jnxWxCommonEventLicenseWillExpire=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,6))
jnxWxCommonEventLicenseWillExpire.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventLicenseWillExpire.setStatus(_A)
jnxWxCommonEventLoginFailure=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,7))
jnxWxCommonEventLoginFailure.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventLoginFailure.setStatus(_A)
jnxWxCommonEventFaultTolerantPassThrough=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,8))
jnxWxCommonEventFaultTolerantPassThrough.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventFaultTolerantPassThrough.setStatus(_A)
jnxWxCommonEventFanFailure=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,9))
jnxWxCommonEventFanFailure.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventFanFailure.setStatus(_A)
jnxWxCommonEventFanSpeedVariation=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,10))
jnxWxCommonEventFanSpeedVariation.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventFanSpeedVariation.setStatus(_A)
jnxWxCommonEventFanOk=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,11))
jnxWxCommonEventFanOk.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventFanOk.setStatus(_A)
jnxWxCommonEventInterfaceSpeedMismatch=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,12))
jnxWxCommonEventInterfaceSpeedMismatch.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventInterfaceSpeedMismatch.setStatus(_A)
jnxWxCommonEventInterfaceSpeedOk=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,13))
jnxWxCommonEventInterfaceSpeedOk.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventInterfaceSpeedOk.setStatus(_A)
jnxWxCommonEventInterfaceDuplexMismatch=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,14))
jnxWxCommonEventInterfaceDuplexMismatch.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventInterfaceDuplexMismatch.setStatus(_A)
jnxWxCommonEventIpsecSecurityAssociationAdded=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,15))
jnxWxCommonEventIpsecSecurityAssociationAdded.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventIpsecSecurityAssociationAdded.setStatus(_A)
jnxWxCommonEventIpsecSecurityAssociationExpired=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,16))
jnxWxCommonEventIpsecSecurityAssociationExpired.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventIpsecSecurityAssociationExpired.setStatus(_A)
jnxWxCommonEventIpsecSecurityAssociationDeleted=NotificationType((1,3,6,1,4,1,8239,2,1,3,2,0,17))
jnxWxCommonEventIpsecSecurityAssociationDeleted.setObjects((_B,_C))
if mibBuilder.loadTexts:jnxWxCommonEventIpsecSecurityAssociationDeleted.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'jnxWxCommonMibModule':jnxWxCommonMibModule,'jnxWxCommonConfMib':jnxWxCommonConfMib,'jnxWxCommonObjs':jnxWxCommonObjs,'jnxWxSys':jnxWxSys,'jnxWxSysSwVersion':jnxWxSysSwVersion,'jnxWxSysHwVersion':jnxWxSysHwVersion,'jnxWxSysSerialNumber':jnxWxSysSerialNumber,'jnxWxSysTimeZoneOffset':jnxWxSysTimeZoneOffset,'jnxWxSysDaylightSaving':jnxWxSysDaylightSaving,'jnxWxChassis':jnxWxChassis,'jnxWxChassisType':jnxWxChassisType,'jnxWxCommonEvents':jnxWxCommonEvents,'jnxWxCommonEventObjs':jnxWxCommonEventObjs,_C:jnxWxCommonEventDescr,'jnxWxCommonEventEvents':jnxWxCommonEventEvents,'jnxWxCommonEventEventsV2':jnxWxCommonEventEventsV2,'jnxWxCommonEventInFailSafeMode':jnxWxCommonEventInFailSafeMode,'jnxWxCommonEventPowerSupplyFailure':jnxWxCommonEventPowerSupplyFailure,'jnxWxCommonEventPowerSupplyOk':jnxWxCommonEventPowerSupplyOk,'jnxWxCommonEventLicenseExpired':jnxWxCommonEventLicenseExpired,'jnxWxCommonEventThruputLimitExceeded':jnxWxCommonEventThruputLimitExceeded,'jnxWxCommonEventLicenseWillExpire':jnxWxCommonEventLicenseWillExpire,'jnxWxCommonEventLoginFailure':jnxWxCommonEventLoginFailure,'jnxWxCommonEventFaultTolerantPassThrough':jnxWxCommonEventFaultTolerantPassThrough,'jnxWxCommonEventFanFailure':jnxWxCommonEventFanFailure,'jnxWxCommonEventFanSpeedVariation':jnxWxCommonEventFanSpeedVariation,'jnxWxCommonEventFanOk':jnxWxCommonEventFanOk,'jnxWxCommonEventInterfaceSpeedMismatch':jnxWxCommonEventInterfaceSpeedMismatch,'jnxWxCommonEventInterfaceSpeedOk':jnxWxCommonEventInterfaceSpeedOk,'jnxWxCommonEventInterfaceDuplexMismatch':jnxWxCommonEventInterfaceDuplexMismatch,'jnxWxCommonEventIpsecSecurityAssociationAdded':jnxWxCommonEventIpsecSecurityAssociationAdded,'jnxWxCommonEventIpsecSecurityAssociationExpired':jnxWxCommonEventIpsecSecurityAssociationExpired,'jnxWxCommonEventIpsecSecurityAssociationDeleted':jnxWxCommonEventIpsecSecurityAssociationDeleted})