_C='Integer32'
_B='mandatory'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_time,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-time')
NTPMode,=mibBuilder.importSymbols('PDN-TC','NTPMode')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
_DevTimeMIBObjects_ObjectIdentity=ObjectIdentity
devTimeMIBObjects=_DevTimeMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,20,1))
_DevTimeAndDate_ObjectIdentity=ObjectIdentity
devTimeAndDate=_DevTimeAndDate_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,20,1,1))
_DevDateAndTime_Type=DateAndTime
_DevDateAndTime_Object=MibScalar
devDateAndTime=_DevDateAndTime_Object((1,3,6,1,4,1,1795,2,24,2,20,1,1,1),_DevDateAndTime_Type())
devDateAndTime.setMaxAccess(_A)
if mibBuilder.loadTexts:devDateAndTime.setStatus(_B)
_DevNTP_ObjectIdentity=ObjectIdentity
devNTP=_DevNTP_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,20,1,2))
_DevNTPServerIP_Type=IpAddress
_DevNTPServerIP_Object=MibScalar
devNTPServerIP=_DevNTPServerIP_Object((1,3,6,1,4,1,1795,2,24,2,20,1,2,1),_DevNTPServerIP_Type())
devNTPServerIP.setMaxAccess(_A)
if mibBuilder.loadTexts:devNTPServerIP.setStatus(_B)
_DevNTPMode_Type=NTPMode
_DevNTPMode_Object=MibScalar
devNTPMode=_DevNTPMode_Object((1,3,6,1,4,1,1795,2,24,2,20,1,2,2),_DevNTPMode_Type())
devNTPMode.setMaxAccess(_A)
if mibBuilder.loadTexts:devNTPMode.setStatus(_B)
class _DevNTPSynchronised_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_DevNTPSynchronised_Type.__name__=_C
_DevNTPSynchronised_Object=MibScalar
devNTPSynchronised=_DevNTPSynchronised_Object((1,3,6,1,4,1,1795,2,24,2,20,1,2,3),_DevNTPSynchronised_Type())
devNTPSynchronised.setMaxAccess(_A)
if mibBuilder.loadTexts:devNTPSynchronised.setStatus(_B)
class _DevNTPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_DevNTPEnable_Type.__name__=_C
_DevNTPEnable_Object=MibScalar
devNTPEnable=_DevNTPEnable_Object((1,3,6,1,4,1,1795,2,24,2,20,1,2,4),_DevNTPEnable_Type())
devNTPEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:devNTPEnable.setStatus(_B)
_DevNTPOffsetFromUTC_Type=Integer32
_DevNTPOffsetFromUTC_Object=MibScalar
devNTPOffsetFromUTC=_DevNTPOffsetFromUTC_Object((1,3,6,1,4,1,1795,2,24,2,20,1,2,5),_DevNTPOffsetFromUTC_Type())
devNTPOffsetFromUTC.setMaxAccess(_A)
if mibBuilder.loadTexts:devNTPOffsetFromUTC.setStatus(_B)
_DevTimeMIBTraps_ObjectIdentity=ObjectIdentity
devTimeMIBTraps=_DevTimeMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,20,2))
mibBuilder.exportSymbols('PDN-DEVICE-TIME-MIB',**{'devTimeMIBObjects':devTimeMIBObjects,'devTimeAndDate':devTimeAndDate,'devDateAndTime':devDateAndTime,'devNTP':devNTP,'devNTPServerIP':devNTPServerIP,'devNTPMode':devNTPMode,'devNTPSynchronised':devNTPSynchronised,'devNTPEnable':devNTPEnable,'devNTPOffsetFromUTC':devNTPOffsetFromUTC,'devTimeMIBTraps':devTimeMIBTraps})