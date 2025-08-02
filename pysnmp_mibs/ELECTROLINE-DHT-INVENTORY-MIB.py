_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhtInventory,=mibBuilder.importSymbols('ELECTROLINE-DHT-ROOT-MIB','dhtInventory')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
_DhtInvHwType_Type=Integer32
_DhtInvHwType_Object=MibScalar
dhtInvHwType=_DhtInvHwType_Object((1,3,6,1,4,1,5802,1,3,1,2,1,1),_DhtInvHwType_Type())
dhtInvHwType.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtInvHwType.setStatus(_A)
_DhtInvHwMinorRev_Type=Integer32
_DhtInvHwMinorRev_Object=MibScalar
dhtInvHwMinorRev=_DhtInvHwMinorRev_Object((1,3,6,1,4,1,5802,1,3,1,2,1,2),_DhtInvHwMinorRev_Type())
dhtInvHwMinorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtInvHwMinorRev.setStatus(_A)
_DhtInvHwMajorRev_Type=Integer32
_DhtInvHwMajorRev_Object=MibScalar
dhtInvHwMajorRev=_DhtInvHwMajorRev_Object((1,3,6,1,4,1,5802,1,3,1,2,1,3),_DhtInvHwMajorRev_Type())
dhtInvHwMajorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtInvHwMajorRev.setStatus(_A)
_DhtInvHwDrvRev_Type=Integer32
_DhtInvHwDrvRev_Object=MibScalar
dhtInvHwDrvRev=_DhtInvHwDrvRev_Object((1,3,6,1,4,1,5802,1,3,1,2,1,4),_DhtInvHwDrvRev_Type())
dhtInvHwDrvRev.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtInvHwDrvRev.setStatus(_A)
class _DhtModelNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhtModelNumber_Type.__name__=_C
_DhtModelNumber_Object=MibScalar
dhtModelNumber=_DhtModelNumber_Object((1,3,6,1,4,1,5802,1,3,1,2,1,5),_DhtModelNumber_Type())
dhtModelNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:dhtModelNumber.setStatus(_A)
_DhtManufacturingInfo_ObjectIdentity=ObjectIdentity
dhtManufacturingInfo=_DhtManufacturingInfo_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,1,10))
if mibBuilder.loadTexts:dhtManufacturingInfo.setStatus(_A)
_DhtMfcDateTime_Type=DateAndTime
_DhtMfcDateTime_Object=MibScalar
dhtMfcDateTime=_DhtMfcDateTime_Object((1,3,6,1,4,1,5802,1,3,1,2,1,10,1),_DhtMfcDateTime_Type())
dhtMfcDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtMfcDateTime.setStatus(_A)
_DhtMfcTestSwVersion_Type=OctetString
_DhtMfcTestSwVersion_Object=MibScalar
dhtMfcTestSwVersion=_DhtMfcTestSwVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,1,10,2),_DhtMfcTestSwVersion_Type())
dhtMfcTestSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtMfcTestSwVersion.setStatus(_A)
_DhtMfcJobNumber_Type=OctetString
_DhtMfcJobNumber_Object=MibScalar
dhtMfcJobNumber=_DhtMfcJobNumber_Object((1,3,6,1,4,1,5802,1,3,1,2,1,10,3),_DhtMfcJobNumber_Type())
dhtMfcJobNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtMfcJobNumber.setStatus(_A)
mibBuilder.exportSymbols('ELECTROLINE-DHT-INVENTORY-MIB',**{'dhtInvHwType':dhtInvHwType,'dhtInvHwMinorRev':dhtInvHwMinorRev,'dhtInvHwMajorRev':dhtInvHwMajorRev,'dhtInvHwDrvRev':dhtInvHwDrvRev,'dhtModelNumber':dhtModelNumber,'dhtManufacturingInfo':dhtManufacturingInfo,'dhtMfcDateTime':dhtMfcDateTime,'dhtMfcTestSwVersion':dhtMfcTestSwVersion,'dhtMfcJobNumber':dhtMfcJobNumber})