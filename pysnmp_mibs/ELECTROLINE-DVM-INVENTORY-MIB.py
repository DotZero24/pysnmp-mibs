_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dvmInventory,=mibBuilder.importSymbols('ELECTROLINE-DVM-ROOT-MIB','dvmInventory')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
_DvmInvHwType_Type=Integer32
_DvmInvHwType_Object=MibScalar
dvmInvHwType=_DvmInvHwType_Object((1,3,6,1,4,1,5802,1,3,1,3,1,1),_DvmInvHwType_Type())
dvmInvHwType.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmInvHwType.setStatus(_A)
_DvmInvHwMinorRev_Type=Integer32
_DvmInvHwMinorRev_Object=MibScalar
dvmInvHwMinorRev=_DvmInvHwMinorRev_Object((1,3,6,1,4,1,5802,1,3,1,3,1,2),_DvmInvHwMinorRev_Type())
dvmInvHwMinorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmInvHwMinorRev.setStatus(_A)
_DvmInvHwMajorRev_Type=Integer32
_DvmInvHwMajorRev_Object=MibScalar
dvmInvHwMajorRev=_DvmInvHwMajorRev_Object((1,3,6,1,4,1,5802,1,3,1,3,1,3),_DvmInvHwMajorRev_Type())
dvmInvHwMajorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmInvHwMajorRev.setStatus(_A)
_DvmInvHwDrvRev_Type=Integer32
_DvmInvHwDrvRev_Object=MibScalar
dvmInvHwDrvRev=_DvmInvHwDrvRev_Object((1,3,6,1,4,1,5802,1,3,1,3,1,4),_DvmInvHwDrvRev_Type())
dvmInvHwDrvRev.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmInvHwDrvRev.setStatus(_A)
class _DvmModelNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DvmModelNumber_Type.__name__=_C
_DvmModelNumber_Object=MibScalar
dvmModelNumber=_DvmModelNumber_Object((1,3,6,1,4,1,5802,1,3,1,3,1,5),_DvmModelNumber_Type())
dvmModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmModelNumber.setStatus(_A)
_DvmManufacturingInfo_ObjectIdentity=ObjectIdentity
dvmManufacturingInfo=_DvmManufacturingInfo_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,1,10))
if mibBuilder.loadTexts:dvmManufacturingInfo.setStatus(_A)
_DvmMfcDateTime_Type=DateAndTime
_DvmMfcDateTime_Object=MibScalar
dvmMfcDateTime=_DvmMfcDateTime_Object((1,3,6,1,4,1,5802,1,3,1,3,1,10,1),_DvmMfcDateTime_Type())
dvmMfcDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmMfcDateTime.setStatus(_A)
_DvmMfcTestSwVersion_Type=OctetString
_DvmMfcTestSwVersion_Object=MibScalar
dvmMfcTestSwVersion=_DvmMfcTestSwVersion_Object((1,3,6,1,4,1,5802,1,3,1,3,1,10,2),_DvmMfcTestSwVersion_Type())
dvmMfcTestSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmMfcTestSwVersion.setStatus(_A)
mibBuilder.exportSymbols('ELECTROLINE-DVM-INVENTORY-MIB',**{'dvmInvHwType':dvmInvHwType,'dvmInvHwMinorRev':dvmInvHwMinorRev,'dvmInvHwMajorRev':dvmInvHwMajorRev,'dvmInvHwDrvRev':dvmInvHwDrvRev,'dvmModelNumber':dvmModelNumber,'dvmManufacturingInfo':dvmManufacturingInfo,'dvmMfcDateTime':dvmMfcDateTime,'dvmMfcTestSwVersion':dvmMfcTestSwVersion})