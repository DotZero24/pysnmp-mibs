_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonInventory,=mibBuilder.importSymbols('ELECTROLINE-COMMON-ROOT-MIB','commonInventory')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
_InvHwType_Type=Integer32
_InvHwType_Object=MibScalar
invHwType=_InvHwType_Object((1,3,6,1,4,1,5802,1,3,1,4,1,1),_InvHwType_Type())
invHwType.setMaxAccess(_B)
if mibBuilder.loadTexts:invHwType.setStatus(_A)
_InvHwMinorRev_Type=Integer32
_InvHwMinorRev_Object=MibScalar
invHwMinorRev=_InvHwMinorRev_Object((1,3,6,1,4,1,5802,1,3,1,4,1,2),_InvHwMinorRev_Type())
invHwMinorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:invHwMinorRev.setStatus(_A)
_InvHwMajorRev_Type=Integer32
_InvHwMajorRev_Object=MibScalar
invHwMajorRev=_InvHwMajorRev_Object((1,3,6,1,4,1,5802,1,3,1,4,1,3),_InvHwMajorRev_Type())
invHwMajorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:invHwMajorRev.setStatus(_A)
_InvHwDrvRev_Type=Integer32
_InvHwDrvRev_Object=MibScalar
invHwDrvRev=_InvHwDrvRev_Object((1,3,6,1,4,1,5802,1,3,1,4,1,4),_InvHwDrvRev_Type())
invHwDrvRev.setMaxAccess(_B)
if mibBuilder.loadTexts:invHwDrvRev.setStatus(_A)
class _ModelNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ModelNumber_Type.__name__=_C
_ModelNumber_Object=MibScalar
modelNumber=_ModelNumber_Object((1,3,6,1,4,1,5802,1,3,1,4,1,5),_ModelNumber_Type())
modelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:modelNumber.setStatus(_A)
_ManufacturingInfo_ObjectIdentity=ObjectIdentity
manufacturingInfo=_ManufacturingInfo_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,4,1,10))
if mibBuilder.loadTexts:manufacturingInfo.setStatus(_A)
_MfcDateTime_Type=DateAndTime
_MfcDateTime_Object=MibScalar
mfcDateTime=_MfcDateTime_Object((1,3,6,1,4,1,5802,1,3,1,4,1,10,1),_MfcDateTime_Type())
mfcDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mfcDateTime.setStatus(_A)
_MfcTestSwVersion_Type=OctetString
_MfcTestSwVersion_Object=MibScalar
mfcTestSwVersion=_MfcTestSwVersion_Object((1,3,6,1,4,1,5802,1,3,1,4,1,10,2),_MfcTestSwVersion_Type())
mfcTestSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mfcTestSwVersion.setStatus(_A)
mibBuilder.exportSymbols('ELECTROLINE-COMMON-INVENTORY-MIB',**{'invHwType':invHwType,'invHwMinorRev':invHwMinorRev,'invHwMajorRev':invHwMajorRev,'invHwDrvRev':invHwDrvRev,'modelNumber':modelNumber,'manufacturingInfo':manufacturingInfo,'mfcDateTime':mfcDateTime,'mfcTestSwVersion':mfcTestSwVersion})