_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmWanGpsMib=ModuleIdentity((1,3,6,1,4,1,248,40,1,7))
if mibBuilder.loadTexts:hmWanGpsMib.setRevisions(('2015-02-13 00:00',))
_HmWanGpsTimeUTC_Type=OctetString
_HmWanGpsTimeUTC_Object=MibScalar
hmWanGpsTimeUTC=_HmWanGpsTimeUTC_Object((1,3,6,1,4,1,248,40,1,7,1),_HmWanGpsTimeUTC_Type())
hmWanGpsTimeUTC.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsTimeUTC.setStatus(_B)
_HmWanGpsLatitude_Type=OctetString
_HmWanGpsLatitude_Object=MibScalar
hmWanGpsLatitude=_HmWanGpsLatitude_Object((1,3,6,1,4,1,248,40,1,7,2),_HmWanGpsLatitude_Type())
hmWanGpsLatitude.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsLatitude.setStatus(_B)
_HmWanGpsLongitude_Type=OctetString
_HmWanGpsLongitude_Object=MibScalar
hmWanGpsLongitude=_HmWanGpsLongitude_Object((1,3,6,1,4,1,248,40,1,7,3),_HmWanGpsLongitude_Type())
hmWanGpsLongitude.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsLongitude.setStatus(_B)
_HmWanGpsAltitude_Type=OctetString
_HmWanGpsAltitude_Object=MibScalar
hmWanGpsAltitude=_HmWanGpsAltitude_Object((1,3,6,1,4,1,248,40,1,7,4),_HmWanGpsAltitude_Type())
hmWanGpsAltitude.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsAltitude.setStatus(_B)
_HmWanGpsSatellites_Type=Integer32
_HmWanGpsSatellites_Object=MibScalar
hmWanGpsSatellites=_HmWanGpsSatellites_Object((1,3,6,1,4,1,248,40,1,7,5),_HmWanGpsSatellites_Type())
hmWanGpsSatellites.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsSatellites.setStatus(_B)
_HmWanGpsFixStatus_Type=OctetString
_HmWanGpsFixStatus_Object=MibScalar
hmWanGpsFixStatus=_HmWanGpsFixStatus_Object((1,3,6,1,4,1,248,40,1,7,6),_HmWanGpsFixStatus_Type())
hmWanGpsFixStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsFixStatus.setStatus(_B)
_HmWanGpsSpeedOverGround_Type=OctetString
_HmWanGpsSpeedOverGround_Object=MibScalar
hmWanGpsSpeedOverGround=_HmWanGpsSpeedOverGround_Object((1,3,6,1,4,1,248,40,1,7,7),_HmWanGpsSpeedOverGround_Type())
hmWanGpsSpeedOverGround.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsSpeedOverGround.setStatus(_B)
_HmWanGpsCourseOverGround_Type=OctetString
_HmWanGpsCourseOverGround_Object=MibScalar
hmWanGpsCourseOverGround=_HmWanGpsCourseOverGround_Object((1,3,6,1,4,1,248,40,1,7,8),_HmWanGpsCourseOverGround_Type())
hmWanGpsCourseOverGround.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsCourseOverGround.setStatus(_B)
_HmWanGpsDate_Type=OctetString
_HmWanGpsDate_Object=MibScalar
hmWanGpsDate=_HmWanGpsDate_Object((1,3,6,1,4,1,248,40,1,7,9),_HmWanGpsDate_Type())
hmWanGpsDate.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanGpsDate.setStatus(_B)
mibBuilder.exportSymbols('HIRSCHMANN-WAN-GPS-MIB',**{'hmWanGpsMib':hmWanGpsMib,'hmWanGpsTimeUTC':hmWanGpsTimeUTC,'hmWanGpsLatitude':hmWanGpsLatitude,'hmWanGpsLongitude':hmWanGpsLongitude,'hmWanGpsAltitude':hmWanGpsAltitude,'hmWanGpsSatellites':hmWanGpsSatellites,'hmWanGpsFixStatus':hmWanGpsFixStatus,'hmWanGpsSpeedOverGround':hmWanGpsSpeedOverGround,'hmWanGpsCourseOverGround':hmWanGpsCourseOverGround,'hmWanGpsDate':hmWanGpsDate})