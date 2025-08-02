_N='intDeciAmpsCT8'
_M='intDeciAmpsCT7'
_L='intDeciAmpsCT6'
_K='intDeciAmpsCT5'
_J='intDeciAmpsCT4'
_I='intDeciAmpsCT3'
_H='intDeciAmpsCT2'
_G='intDeciAmpsCT1'
_F='NotificationType'
_E='0.1 Amps'
_D='EATON-GENESIS-II-MIB'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Eaton_ObjectIdentity=ObjectIdentity
eaton=_Eaton_ObjectIdentity((1,3,6,1,4,1,17373))
_Genesis2_ObjectIdentity=ObjectIdentity
genesis2=_Genesis2_ObjectIdentity((1,3,6,1,4,1,17373,3))
_ProductInfo_ObjectIdentity=ObjectIdentity
productInfo=_ProductInfo_ObjectIdentity((1,3,6,1,4,1,17373,3,1))
_ProductTitle_Type=DisplayString
_ProductTitle_Object=MibScalar
productTitle=_ProductTitle_Object((1,3,6,1,4,1,17373,3,1,1),_ProductTitle_Type())
productTitle.setMaxAccess(_A)
if mibBuilder.loadTexts:productTitle.setStatus(_B)
_ProductVersion_Type=DisplayString
_ProductVersion_Object=MibScalar
productVersion=_ProductVersion_Object((1,3,6,1,4,1,17373,3,1,2),_ProductVersion_Type())
productVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:productVersion.setStatus(_B)
_ProductName_Type=DisplayString
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,17373,3,1,3),_ProductName_Type())
productName.setMaxAccess(_A)
if mibBuilder.loadTexts:productName.setStatus(_B)
_ProductMAC_Type=DisplayString
_ProductMAC_Object=MibScalar
productMAC=_ProductMAC_Object((1,3,6,1,4,1,17373,3,1,4),_ProductMAC_Type())
productMAC.setMaxAccess(_A)
if mibBuilder.loadTexts:productMAC.setStatus(_B)
_ProductIP_Type=DisplayString
_ProductIP_Object=MibScalar
productIP=_ProductIP_Object((1,3,6,1,4,1,17373,3,1,5),_ProductIP_Type())
productIP.setMaxAccess(_A)
if mibBuilder.loadTexts:productIP.setStatus(_B)
_SensorData_ObjectIdentity=ObjectIdentity
sensorData=_SensorData_ObjectIdentity((1,3,6,1,4,1,17373,3,2))
class _IntDeciAmpsCT1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT1_Type.__name__=_C
_IntDeciAmpsCT1_Object=MibScalar
intDeciAmpsCT1=_IntDeciAmpsCT1_Object((1,3,6,1,4,1,17373,3,2,1),_IntDeciAmpsCT1_Type())
intDeciAmpsCT1.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT1.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT1.setUnits(_E)
class _IntDeciAmpsCT2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT2_Type.__name__=_C
_IntDeciAmpsCT2_Object=MibScalar
intDeciAmpsCT2=_IntDeciAmpsCT2_Object((1,3,6,1,4,1,17373,3,2,2),_IntDeciAmpsCT2_Type())
intDeciAmpsCT2.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT2.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT2.setUnits(_E)
class _IntDeciAmpsCT3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT3_Type.__name__=_C
_IntDeciAmpsCT3_Object=MibScalar
intDeciAmpsCT3=_IntDeciAmpsCT3_Object((1,3,6,1,4,1,17373,3,2,3),_IntDeciAmpsCT3_Type())
intDeciAmpsCT3.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT3.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT3.setUnits(_E)
class _IntDeciAmpsCT4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT4_Type.__name__=_C
_IntDeciAmpsCT4_Object=MibScalar
intDeciAmpsCT4=_IntDeciAmpsCT4_Object((1,3,6,1,4,1,17373,3,2,4),_IntDeciAmpsCT4_Type())
intDeciAmpsCT4.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT4.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT4.setUnits(_E)
class _IntDeciAmpsCT5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT5_Type.__name__=_C
_IntDeciAmpsCT5_Object=MibScalar
intDeciAmpsCT5=_IntDeciAmpsCT5_Object((1,3,6,1,4,1,17373,3,2,5),_IntDeciAmpsCT5_Type())
intDeciAmpsCT5.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT5.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT5.setUnits(_E)
class _IntDeciAmpsCT6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT6_Type.__name__=_C
_IntDeciAmpsCT6_Object=MibScalar
intDeciAmpsCT6=_IntDeciAmpsCT6_Object((1,3,6,1,4,1,17373,3,2,6),_IntDeciAmpsCT6_Type())
intDeciAmpsCT6.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT6.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT6.setUnits(_E)
class _IntDeciAmpsCT7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT7_Type.__name__=_C
_IntDeciAmpsCT7_Object=MibScalar
intDeciAmpsCT7=_IntDeciAmpsCT7_Object((1,3,6,1,4,1,17373,3,2,7),_IntDeciAmpsCT7_Type())
intDeciAmpsCT7.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT7.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT7.setUnits(_E)
class _IntDeciAmpsCT8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_IntDeciAmpsCT8_Type.__name__=_C
_IntDeciAmpsCT8_Object=MibScalar
intDeciAmpsCT8=_IntDeciAmpsCT8_Object((1,3,6,1,4,1,17373,3,2,8),_IntDeciAmpsCT8_Type())
intDeciAmpsCT8.setMaxAccess(_A)
if mibBuilder.loadTexts:intDeciAmpsCT8.setStatus(_B)
if mibBuilder.loadTexts:intDeciAmpsCT8.setUnits(_E)
intDeciAmpsCT1TRAP=NotificationType((1,3,6,1,4,1,17373,0,1))
intDeciAmpsCT1TRAP.setObjects((_D,_G))
if mibBuilder.loadTexts:intDeciAmpsCT1TRAP.setStatus('')
intDeciAmpsCT2TRAP=NotificationType((1,3,6,1,4,1,17373,0,2))
intDeciAmpsCT2TRAP.setObjects((_D,_H))
if mibBuilder.loadTexts:intDeciAmpsCT2TRAP.setStatus('')
intDeciAmpsCT3TRAP=NotificationType((1,3,6,1,4,1,17373,0,3))
intDeciAmpsCT3TRAP.setObjects((_D,_I))
if mibBuilder.loadTexts:intDeciAmpsCT3TRAP.setStatus('')
intDeciAmpsCT4TRAP=NotificationType((1,3,6,1,4,1,17373,0,4))
intDeciAmpsCT4TRAP.setObjects((_D,_J))
if mibBuilder.loadTexts:intDeciAmpsCT4TRAP.setStatus('')
intDeciAmpsCT5TRAP=NotificationType((1,3,6,1,4,1,17373,0,5))
intDeciAmpsCT5TRAP.setObjects((_D,_K))
if mibBuilder.loadTexts:intDeciAmpsCT5TRAP.setStatus('')
intDeciAmpsCT6TRAP=NotificationType((1,3,6,1,4,1,17373,0,6))
intDeciAmpsCT6TRAP.setObjects((_D,_L))
if mibBuilder.loadTexts:intDeciAmpsCT6TRAP.setStatus('')
intDeciAmpsCT7TRAP=NotificationType((1,3,6,1,4,1,17373,0,7))
intDeciAmpsCT7TRAP.setObjects((_D,_M))
if mibBuilder.loadTexts:intDeciAmpsCT7TRAP.setStatus('')
intDeciAmpsCT8TRAP=NotificationType((1,3,6,1,4,1,17373,0,8))
intDeciAmpsCT8TRAP.setObjects((_D,_N))
if mibBuilder.loadTexts:intDeciAmpsCT8TRAP.setStatus('')
mibBuilder.exportSymbols(_D,**{'eaton':eaton,'intDeciAmpsCT1TRAP':intDeciAmpsCT1TRAP,'intDeciAmpsCT2TRAP':intDeciAmpsCT2TRAP,'intDeciAmpsCT3TRAP':intDeciAmpsCT3TRAP,'intDeciAmpsCT4TRAP':intDeciAmpsCT4TRAP,'intDeciAmpsCT5TRAP':intDeciAmpsCT5TRAP,'intDeciAmpsCT6TRAP':intDeciAmpsCT6TRAP,'intDeciAmpsCT7TRAP':intDeciAmpsCT7TRAP,'intDeciAmpsCT8TRAP':intDeciAmpsCT8TRAP,'genesis2':genesis2,'productInfo':productInfo,'productTitle':productTitle,'productVersion':productVersion,'productName':productName,'productMAC':productMAC,'productIP':productIP,'sensorData':sensorData,_G:intDeciAmpsCT1,_H:intDeciAmpsCT2,_I:intDeciAmpsCT3,_J:intDeciAmpsCT4,_K:intDeciAmpsCT5,_L:intDeciAmpsCT6,_M:intDeciAmpsCT7,_N:intDeciAmpsCT8})