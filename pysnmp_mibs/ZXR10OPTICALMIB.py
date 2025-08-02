_G='zxr10OpticalIfIndex'
_F='ZXR10OPTICALMIB'
_E='m-1000'
_D='null'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
zxr10interfaces,=mibBuilder.importSymbols('ZXR10-SMI','zxr10interfaces')
zxr10OpticalMIB=ModuleIdentity((1,3,6,1,4,1,3902,3,103,11))
class DisplayString(OctetString):0
class OpticalOnline(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('offline',0),('online',1)))
class SonetComplianceCodesType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_D,0),('short-reach',1),('intermediate-reach',2),('long-reach',4),('very-Long-reach',8)))
class SonetComplianceCodesSpeed(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8)));namedValues=NamedValues(*(('oc3',1),('oc12',2),('oc48',4),('oc192',8)))
class GigabitEthernetComplianceCodesType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,0),('base-sx-1000',1),('base-lx-1000',2),('base-lx-100',3),('base-cx-1000',4),('base-fx-100',5),('base_bx',6),('base_px',7),('base-t-1000',8),('base-t-100',9)))
class InfinibandComplianceCodesType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_D,0),('copper-Passiv',1),('copper-Active',2),('lx',4),('sx',8)))
class GigabitEthernetComplianceCodesSpeed(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('g-10',2),('g-40',3),('g-100',4)))
class InfinibandComplianceCodesSpeed(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('g-10',2)))
_Zxr10OpticalTable_Object=MibTable
zxr10OpticalTable=_Zxr10OpticalTable_Object((1,3,6,1,4,1,3902,3,103,11,1))
if mibBuilder.loadTexts:zxr10OpticalTable.setStatus(_A)
_Zxr10OpticalEntry_Object=MibTableRow
zxr10OpticalEntry=_Zxr10OpticalEntry_Object((1,3,6,1,4,1,3902,3,103,11,1,1))
zxr10OpticalEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxr10OpticalEntry.setStatus(_A)
_Zxr10OpticalIfIndex_Type=Integer32
_Zxr10OpticalIfIndex_Object=MibTableColumn
zxr10OpticalIfIndex=_Zxr10OpticalIfIndex_Object((1,3,6,1,4,1,3902,3,103,11,1,1,1),_Zxr10OpticalIfIndex_Type())
zxr10OpticalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalIfIndex.setStatus(_A)
class _Zxr10OpticalIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalIfName_Type.__name__=_C
_Zxr10OpticalIfName_Object=MibTableColumn
zxr10OpticalIfName=_Zxr10OpticalIfName_Object((1,3,6,1,4,1,3902,3,103,11,1,1,2),_Zxr10OpticalIfName_Type())
zxr10OpticalIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalIfName.setStatus(_A)
_Zxr10OpticalOnline_Type=OpticalOnline
_Zxr10OpticalOnline_Object=MibTableColumn
zxr10OpticalOnline=_Zxr10OpticalOnline_Object((1,3,6,1,4,1,3902,3,103,11,1,1,3),_Zxr10OpticalOnline_Type())
zxr10OpticalOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalOnline.setStatus(_A)
class _Zxr10OpticalFpType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalFpType_Type.__name__=_C
_Zxr10OpticalFpType_Object=MibTableColumn
zxr10OpticalFpType=_Zxr10OpticalFpType_Object((1,3,6,1,4,1,3902,3,103,11,1,1,4),_Zxr10OpticalFpType_Type())
zxr10OpticalFpType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalFpType.setStatus(_A)
_Zxr10OpticalSonetComplianceCodesType_Type=SonetComplianceCodesType
_Zxr10OpticalSonetComplianceCodesType_Object=MibTableColumn
zxr10OpticalSonetComplianceCodesType=_Zxr10OpticalSonetComplianceCodesType_Object((1,3,6,1,4,1,3902,3,103,11,1,1,5),_Zxr10OpticalSonetComplianceCodesType_Type())
zxr10OpticalSonetComplianceCodesType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSonetComplianceCodesType.setStatus(_A)
_Zxr10OpticalSonetComplianceCodesSpeed_Type=SonetComplianceCodesSpeed
_Zxr10OpticalSonetComplianceCodesSpeed_Object=MibTableColumn
zxr10OpticalSonetComplianceCodesSpeed=_Zxr10OpticalSonetComplianceCodesSpeed_Object((1,3,6,1,4,1,3902,3,103,11,1,1,6),_Zxr10OpticalSonetComplianceCodesSpeed_Type())
zxr10OpticalSonetComplianceCodesSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSonetComplianceCodesSpeed.setStatus(_A)
_Zxr10OpticalGigabitEthernetComplianceCodesType_Type=DisplayString
_Zxr10OpticalGigabitEthernetComplianceCodesType_Object=MibTableColumn
zxr10OpticalGigabitEthernetComplianceCodesType=_Zxr10OpticalGigabitEthernetComplianceCodesType_Object((1,3,6,1,4,1,3902,3,103,11,1,1,7),_Zxr10OpticalGigabitEthernetComplianceCodesType_Type())
zxr10OpticalGigabitEthernetComplianceCodesType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalGigabitEthernetComplianceCodesType.setStatus(_A)
_Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Type=GigabitEthernetComplianceCodesSpeed
_Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Object=MibTableColumn
zxr10OpticalGigabitEthernetComplianceCodesSpeed=_Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Object((1,3,6,1,4,1,3902,3,103,11,1,1,8),_Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Type())
zxr10OpticalGigabitEthernetComplianceCodesSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalGigabitEthernetComplianceCodesSpeed.setStatus(_A)
_Zxr10OpticalInfinibandComplianceCodesType_Type=InfinibandComplianceCodesType
_Zxr10OpticalInfinibandComplianceCodesType_Object=MibTableColumn
zxr10OpticalInfinibandComplianceCodesType=_Zxr10OpticalInfinibandComplianceCodesType_Object((1,3,6,1,4,1,3902,3,103,11,1,1,9),_Zxr10OpticalInfinibandComplianceCodesType_Type())
zxr10OpticalInfinibandComplianceCodesType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalInfinibandComplianceCodesType.setStatus(_A)
_Zxr10OpticalInfinibandComplianceCodesSpeed_Type=InfinibandComplianceCodesSpeed
_Zxr10OpticalInfinibandComplianceCodesSpeed_Object=MibTableColumn
zxr10OpticalInfinibandComplianceCodesSpeed=_Zxr10OpticalInfinibandComplianceCodesSpeed_Object((1,3,6,1,4,1,3902,3,103,11,1,1,10),_Zxr10OpticalInfinibandComplianceCodesSpeed_Type())
zxr10OpticalInfinibandComplianceCodesSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalInfinibandComplianceCodesSpeed.setStatus(_A)
_Zxr10OpticalDisSMFkm_Type=Integer32
_Zxr10OpticalDisSMFkm_Object=MibTableColumn
zxr10OpticalDisSMFkm=_Zxr10OpticalDisSMFkm_Object((1,3,6,1,4,1,3902,3,103,11,1,1,11),_Zxr10OpticalDisSMFkm_Type())
zxr10OpticalDisSMFkm.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalDisSMFkm.setStatus(_A)
_Zxr10OpticalDis9um_Type=Integer32
_Zxr10OpticalDis9um_Object=MibTableColumn
zxr10OpticalDis9um=_Zxr10OpticalDis9um_Object((1,3,6,1,4,1,3902,3,103,11,1,1,12),_Zxr10OpticalDis9um_Type())
zxr10OpticalDis9um.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalDis9um.setStatus(_A)
_Zxr10OpticalDis50um_Type=Integer32
_Zxr10OpticalDis50um_Object=MibTableColumn
zxr10OpticalDis50um=_Zxr10OpticalDis50um_Object((1,3,6,1,4,1,3902,3,103,11,1,1,13),_Zxr10OpticalDis50um_Type())
zxr10OpticalDis50um.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalDis50um.setStatus(_A)
_Zxr10OpticalDis62um_Type=Integer32
_Zxr10OpticalDis62um_Object=MibTableColumn
zxr10OpticalDis62um=_Zxr10OpticalDis62um_Object((1,3,6,1,4,1,3902,3,103,11,1,1,14),_Zxr10OpticalDis62um_Type())
zxr10OpticalDis62um.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalDis62um.setStatus(_A)
_Zxr10OpticalDiscopperLine_Type=Integer32
_Zxr10OpticalDiscopperLine_Object=MibTableColumn
zxr10OpticalDiscopperLine=_Zxr10OpticalDiscopperLine_Object((1,3,6,1,4,1,3902,3,103,11,1,1,15),_Zxr10OpticalDiscopperLine_Type())
zxr10OpticalDiscopperLine.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalDiscopperLine.setStatus(_A)
_Zxr10OpticalSWaveLenth_Type=DisplayString
_Zxr10OpticalSWaveLenth_Object=MibTableColumn
zxr10OpticalSWaveLenth=_Zxr10OpticalSWaveLenth_Object((1,3,6,1,4,1,3902,3,103,11,1,1,16),_Zxr10OpticalSWaveLenth_Type())
zxr10OpticalSWaveLenth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSWaveLenth.setStatus(_A)
_Zxr10OpticalSWaveLenthValid_Type=Integer32
_Zxr10OpticalSWaveLenthValid_Object=MibTableColumn
zxr10OpticalSWaveLenthValid=_Zxr10OpticalSWaveLenthValid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,17),_Zxr10OpticalSWaveLenthValid_Type())
zxr10OpticalSWaveLenthValid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSWaveLenthValid.setStatus(_A)
class _Zxr10OpticalSRxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSRxPower_Type.__name__=_C
_Zxr10OpticalSRxPower_Object=MibTableColumn
zxr10OpticalSRxPower=_Zxr10OpticalSRxPower_Object((1,3,6,1,4,1,3902,3,103,11,1,1,18),_Zxr10OpticalSRxPower_Type())
zxr10OpticalSRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPower.setStatus(_A)
_Zxr10OpticalSRxPowerValid_Type=Integer32
_Zxr10OpticalSRxPowerValid_Object=MibTableColumn
zxr10OpticalSRxPowerValid=_Zxr10OpticalSRxPowerValid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,19),_Zxr10OpticalSRxPowerValid_Type())
zxr10OpticalSRxPowerValid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerValid.setStatus(_A)
class _Zxr10OpticalSTxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxPower_Type.__name__=_C
_Zxr10OpticalSTxPower_Object=MibTableColumn
zxr10OpticalSTxPower=_Zxr10OpticalSTxPower_Object((1,3,6,1,4,1,3902,3,103,11,1,1,20),_Zxr10OpticalSTxPower_Type())
zxr10OpticalSTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPower.setStatus(_A)
_Zxr10OpticalSTxPowerValid_Type=Integer32
_Zxr10OpticalSTxPowerValid_Object=MibTableColumn
zxr10OpticalSTxPowerValid=_Zxr10OpticalSTxPowerValid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,21),_Zxr10OpticalSTxPowerValid_Type())
zxr10OpticalSTxPowerValid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerValid.setStatus(_A)
class _Zxr10OpticalSTxCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxCurrent_Type.__name__=_C
_Zxr10OpticalSTxCurrent_Object=MibTableColumn
zxr10OpticalSTxCurrent=_Zxr10OpticalSTxCurrent_Object((1,3,6,1,4,1,3902,3,103,11,1,1,22),_Zxr10OpticalSTxCurrent_Type())
zxr10OpticalSTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrent.setStatus(_A)
_Zxr10OpticalSTxCurrentValid_Type=Integer32
_Zxr10OpticalSTxCurrentValid_Object=MibTableColumn
zxr10OpticalSTxCurrentValid=_Zxr10OpticalSTxCurrentValid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,23),_Zxr10OpticalSTxCurrentValid_Type())
zxr10OpticalSTxCurrentValid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentValid.setStatus(_A)
class _Zxr10OpticalSTemperature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTemperature_Type.__name__=_C
_Zxr10OpticalSTemperature_Object=MibTableColumn
zxr10OpticalSTemperature=_Zxr10OpticalSTemperature_Object((1,3,6,1,4,1,3902,3,103,11,1,1,24),_Zxr10OpticalSTemperature_Type())
zxr10OpticalSTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperature.setStatus(_A)
_Zxr10OpticalSTemperatureValid_Type=Integer32
_Zxr10OpticalSTemperatureValid_Object=MibTableColumn
zxr10OpticalSTemperatureValid=_Zxr10OpticalSTemperatureValid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,25),_Zxr10OpticalSTemperatureValid_Type())
zxr10OpticalSTemperatureValid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureValid.setStatus(_A)
class _Zxr10Optical33SVoltage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10Optical33SVoltage_Type.__name__=_C
_Zxr10Optical33SVoltage_Object=MibTableColumn
zxr10Optical33SVoltage=_Zxr10Optical33SVoltage_Object((1,3,6,1,4,1,3902,3,103,11,1,1,26),_Zxr10Optical33SVoltage_Type())
zxr10Optical33SVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10Optical33SVoltage.setStatus(_A)
_Zxr10Optical33SVoltageValid_Type=Integer32
_Zxr10Optical33SVoltageValid_Object=MibTableColumn
zxr10Optical33SVoltageValid=_Zxr10Optical33SVoltageValid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,27),_Zxr10Optical33SVoltageValid_Type())
zxr10Optical33SVoltageValid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10Optical33SVoltageValid.setStatus(_A)
class _Zxr10Optical5SVoltage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10Optical5SVoltage_Type.__name__=_C
_Zxr10Optical5SVoltage_Object=MibTableColumn
zxr10Optical5SVoltage=_Zxr10Optical5SVoltage_Object((1,3,6,1,4,1,3902,3,103,11,1,1,28),_Zxr10Optical5SVoltage_Type())
zxr10Optical5SVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10Optical5SVoltage.setStatus(_A)
_Zxr10Optical5SVoltageValid_Type=Integer32
_Zxr10Optical5SVoltageValid_Object=MibTableColumn
zxr10Optical5SVoltageValid=_Zxr10Optical5SVoltageValid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,29),_Zxr10Optical5SVoltageValid_Type())
zxr10Optical5SVoltageValid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10Optical5SVoltageValid.setStatus(_A)
class _Zxr10OpticalVName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalVName_Type.__name__=_C
_Zxr10OpticalVName_Object=MibTableColumn
zxr10OpticalVName=_Zxr10OpticalVName_Object((1,3,6,1,4,1,3902,3,103,11,1,1,30),_Zxr10OpticalVName_Type())
zxr10OpticalVName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalVName.setStatus(_A)
class _Zxr10OpticalVPn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalVPn_Type.__name__=_C
_Zxr10OpticalVPn_Object=MibTableColumn
zxr10OpticalVPn=_Zxr10OpticalVPn_Object((1,3,6,1,4,1,3902,3,103,11,1,1,31),_Zxr10OpticalVPn_Type())
zxr10OpticalVPn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalVPn.setStatus(_A)
class _Zxr10OpticalRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalRev_Type.__name__=_C
_Zxr10OpticalRev_Object=MibTableColumn
zxr10OpticalRev=_Zxr10OpticalRev_Object((1,3,6,1,4,1,3902,3,103,11,1,1,32),_Zxr10OpticalRev_Type())
zxr10OpticalRev.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalRev.setStatus(_A)
class _Zxr10OpticalVSn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalVSn_Type.__name__=_C
_Zxr10OpticalVSn_Object=MibTableColumn
zxr10OpticalVSn=_Zxr10OpticalVSn_Object((1,3,6,1,4,1,3902,3,103,11,1,1,33),_Zxr10OpticalVSn_Type())
zxr10OpticalVSn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalVSn.setStatus(_A)
class _Zxr10OpticalSRxPowerChannel1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSRxPowerChannel1_Type.__name__=_C
_Zxr10OpticalSRxPowerChannel1_Object=MibTableColumn
zxr10OpticalSRxPowerChannel1=_Zxr10OpticalSRxPowerChannel1_Object((1,3,6,1,4,1,3902,3,103,11,1,1,34),_Zxr10OpticalSRxPowerChannel1_Type())
zxr10OpticalSRxPowerChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel1.setStatus(_A)
_Zxr10OpticalSRxPowerChannel1Valid_Type=Integer32
_Zxr10OpticalSRxPowerChannel1Valid_Object=MibTableColumn
zxr10OpticalSRxPowerChannel1Valid=_Zxr10OpticalSRxPowerChannel1Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,35),_Zxr10OpticalSRxPowerChannel1Valid_Type())
zxr10OpticalSRxPowerChannel1Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel1Valid.setStatus(_A)
class _Zxr10OpticalSRxPowerChannel2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSRxPowerChannel2_Type.__name__=_C
_Zxr10OpticalSRxPowerChannel2_Object=MibTableColumn
zxr10OpticalSRxPowerChannel2=_Zxr10OpticalSRxPowerChannel2_Object((1,3,6,1,4,1,3902,3,103,11,1,1,36),_Zxr10OpticalSRxPowerChannel2_Type())
zxr10OpticalSRxPowerChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel2.setStatus(_A)
_Zxr10OpticalSRxPowerChannel2Valid_Type=Integer32
_Zxr10OpticalSRxPowerChannel2Valid_Object=MibTableColumn
zxr10OpticalSRxPowerChannel2Valid=_Zxr10OpticalSRxPowerChannel2Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,37),_Zxr10OpticalSRxPowerChannel2Valid_Type())
zxr10OpticalSRxPowerChannel2Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel2Valid.setStatus(_A)
class _Zxr10OpticalSRxPowerChannel3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSRxPowerChannel3_Type.__name__=_C
_Zxr10OpticalSRxPowerChannel3_Object=MibTableColumn
zxr10OpticalSRxPowerChannel3=_Zxr10OpticalSRxPowerChannel3_Object((1,3,6,1,4,1,3902,3,103,11,1,1,38),_Zxr10OpticalSRxPowerChannel3_Type())
zxr10OpticalSRxPowerChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel3.setStatus(_A)
_Zxr10OpticalSRxPowerChannel3Valid_Type=Integer32
_Zxr10OpticalSRxPowerChannel3Valid_Object=MibTableColumn
zxr10OpticalSRxPowerChannel3Valid=_Zxr10OpticalSRxPowerChannel3Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,39),_Zxr10OpticalSRxPowerChannel3Valid_Type())
zxr10OpticalSRxPowerChannel3Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel3Valid.setStatus(_A)
class _Zxr10OpticalSRxPowerChannel4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSRxPowerChannel4_Type.__name__=_C
_Zxr10OpticalSRxPowerChannel4_Object=MibTableColumn
zxr10OpticalSRxPowerChannel4=_Zxr10OpticalSRxPowerChannel4_Object((1,3,6,1,4,1,3902,3,103,11,1,1,40),_Zxr10OpticalSRxPowerChannel4_Type())
zxr10OpticalSRxPowerChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel4.setStatus(_A)
_Zxr10OpticalSRxPowerChannel4Valid_Type=Integer32
_Zxr10OpticalSRxPowerChannel4Valid_Object=MibTableColumn
zxr10OpticalSRxPowerChannel4Valid=_Zxr10OpticalSRxPowerChannel4Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,41),_Zxr10OpticalSRxPowerChannel4Valid_Type())
zxr10OpticalSRxPowerChannel4Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSRxPowerChannel4Valid.setStatus(_A)
class _Zxr10OpticalSTxPowerChannel1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxPowerChannel1_Type.__name__=_C
_Zxr10OpticalSTxPowerChannel1_Object=MibTableColumn
zxr10OpticalSTxPowerChannel1=_Zxr10OpticalSTxPowerChannel1_Object((1,3,6,1,4,1,3902,3,103,11,1,1,42),_Zxr10OpticalSTxPowerChannel1_Type())
zxr10OpticalSTxPowerChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel1.setStatus(_A)
_Zxr10OpticalSTxPowerChannel1Valid_Type=Integer32
_Zxr10OpticalSTxPowerChannel1Valid_Object=MibTableColumn
zxr10OpticalSTxPowerChannel1Valid=_Zxr10OpticalSTxPowerChannel1Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,43),_Zxr10OpticalSTxPowerChannel1Valid_Type())
zxr10OpticalSTxPowerChannel1Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel1Valid.setStatus(_A)
class _Zxr10OpticalSTxPowerChannel2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxPowerChannel2_Type.__name__=_C
_Zxr10OpticalSTxPowerChannel2_Object=MibTableColumn
zxr10OpticalSTxPowerChannel2=_Zxr10OpticalSTxPowerChannel2_Object((1,3,6,1,4,1,3902,3,103,11,1,1,44),_Zxr10OpticalSTxPowerChannel2_Type())
zxr10OpticalSTxPowerChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel2.setStatus(_A)
_Zxr10OpticalSTxPowerChannel2Valid_Type=Integer32
_Zxr10OpticalSTxPowerChannel2Valid_Object=MibTableColumn
zxr10OpticalSTxPowerChannel2Valid=_Zxr10OpticalSTxPowerChannel2Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,45),_Zxr10OpticalSTxPowerChannel2Valid_Type())
zxr10OpticalSTxPowerChannel2Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel2Valid.setStatus(_A)
class _Zxr10OpticalSTxPowerChannel3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxPowerChannel3_Type.__name__=_C
_Zxr10OpticalSTxPowerChannel3_Object=MibTableColumn
zxr10OpticalSTxPowerChannel3=_Zxr10OpticalSTxPowerChannel3_Object((1,3,6,1,4,1,3902,3,103,11,1,1,46),_Zxr10OpticalSTxPowerChannel3_Type())
zxr10OpticalSTxPowerChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel3.setStatus(_A)
_Zxr10OpticalSTxPowerChannel3Valid_Type=Integer32
_Zxr10OpticalSTxPowerChannel3Valid_Object=MibTableColumn
zxr10OpticalSTxPowerChannel3Valid=_Zxr10OpticalSTxPowerChannel3Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,47),_Zxr10OpticalSTxPowerChannel3Valid_Type())
zxr10OpticalSTxPowerChannel3Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel3Valid.setStatus(_A)
class _Zxr10OpticalSTxPowerChannel4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxPowerChannel4_Type.__name__=_C
_Zxr10OpticalSTxPowerChannel4_Object=MibTableColumn
zxr10OpticalSTxPowerChannel4=_Zxr10OpticalSTxPowerChannel4_Object((1,3,6,1,4,1,3902,3,103,11,1,1,48),_Zxr10OpticalSTxPowerChannel4_Type())
zxr10OpticalSTxPowerChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel4.setStatus(_A)
_Zxr10OpticalSTxPowerChannel4Valid_Type=Integer32
_Zxr10OpticalSTxPowerChannel4Valid_Object=MibTableColumn
zxr10OpticalSTxPowerChannel4Valid=_Zxr10OpticalSTxPowerChannel4Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,49),_Zxr10OpticalSTxPowerChannel4Valid_Type())
zxr10OpticalSTxPowerChannel4Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxPowerChannel4Valid.setStatus(_A)
class _Zxr10OpticalSTxCurrentChannel1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxCurrentChannel1_Type.__name__=_C
_Zxr10OpticalSTxCurrentChannel1_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel1=_Zxr10OpticalSTxCurrentChannel1_Object((1,3,6,1,4,1,3902,3,103,11,1,1,50),_Zxr10OpticalSTxCurrentChannel1_Type())
zxr10OpticalSTxCurrentChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel1.setStatus(_A)
_Zxr10OpticalSTxCurrentChannel1Valid_Type=Integer32
_Zxr10OpticalSTxCurrentChannel1Valid_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel1Valid=_Zxr10OpticalSTxCurrentChannel1Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,51),_Zxr10OpticalSTxCurrentChannel1Valid_Type())
zxr10OpticalSTxCurrentChannel1Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel1Valid.setStatus(_A)
class _Zxr10OpticalSTxCurrentChannel2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxCurrentChannel2_Type.__name__=_C
_Zxr10OpticalSTxCurrentChannel2_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel2=_Zxr10OpticalSTxCurrentChannel2_Object((1,3,6,1,4,1,3902,3,103,11,1,1,52),_Zxr10OpticalSTxCurrentChannel2_Type())
zxr10OpticalSTxCurrentChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel2.setStatus(_A)
_Zxr10OpticalSTxCurrentChannel2Valid_Type=Integer32
_Zxr10OpticalSTxCurrentChannel2Valid_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel2Valid=_Zxr10OpticalSTxCurrentChannel2Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,53),_Zxr10OpticalSTxCurrentChannel2Valid_Type())
zxr10OpticalSTxCurrentChannel2Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel2Valid.setStatus(_A)
class _Zxr10OpticalSTxCurrentChannel3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxCurrentChannel3_Type.__name__=_C
_Zxr10OpticalSTxCurrentChannel3_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel3=_Zxr10OpticalSTxCurrentChannel3_Object((1,3,6,1,4,1,3902,3,103,11,1,1,54),_Zxr10OpticalSTxCurrentChannel3_Type())
zxr10OpticalSTxCurrentChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel3.setStatus(_A)
_Zxr10OpticalSTxCurrentChannel3Valid_Type=Integer32
_Zxr10OpticalSTxCurrentChannel3Valid_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel3Valid=_Zxr10OpticalSTxCurrentChannel3Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,55),_Zxr10OpticalSTxCurrentChannel3Valid_Type())
zxr10OpticalSTxCurrentChannel3Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel3Valid.setStatus(_A)
class _Zxr10OpticalSTxCurrentChannel4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTxCurrentChannel4_Type.__name__=_C
_Zxr10OpticalSTxCurrentChannel4_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel4=_Zxr10OpticalSTxCurrentChannel4_Object((1,3,6,1,4,1,3902,3,103,11,1,1,56),_Zxr10OpticalSTxCurrentChannel4_Type())
zxr10OpticalSTxCurrentChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel4.setStatus(_A)
_Zxr10OpticalSTxCurrentChannel4Valid_Type=Integer32
_Zxr10OpticalSTxCurrentChannel4Valid_Object=MibTableColumn
zxr10OpticalSTxCurrentChannel4Valid=_Zxr10OpticalSTxCurrentChannel4Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,57),_Zxr10OpticalSTxCurrentChannel4Valid_Type())
zxr10OpticalSTxCurrentChannel4Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTxCurrentChannel4Valid.setStatus(_A)
class _Zxr10OpticalSTemperatureChannel1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTemperatureChannel1_Type.__name__=_C
_Zxr10OpticalSTemperatureChannel1_Object=MibTableColumn
zxr10OpticalSTemperatureChannel1=_Zxr10OpticalSTemperatureChannel1_Object((1,3,6,1,4,1,3902,3,103,11,1,1,58),_Zxr10OpticalSTemperatureChannel1_Type())
zxr10OpticalSTemperatureChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel1.setStatus(_A)
_Zxr10OpticalSTemperatureChannel1Valid_Type=Integer32
_Zxr10OpticalSTemperatureChannel1Valid_Object=MibTableColumn
zxr10OpticalSTemperatureChannel1Valid=_Zxr10OpticalSTemperatureChannel1Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,59),_Zxr10OpticalSTemperatureChannel1Valid_Type())
zxr10OpticalSTemperatureChannel1Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel1Valid.setStatus(_A)
class _Zxr10OpticalSTemperatureChannel2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTemperatureChannel2_Type.__name__=_C
_Zxr10OpticalSTemperatureChannel2_Object=MibTableColumn
zxr10OpticalSTemperatureChannel2=_Zxr10OpticalSTemperatureChannel2_Object((1,3,6,1,4,1,3902,3,103,11,1,1,60),_Zxr10OpticalSTemperatureChannel2_Type())
zxr10OpticalSTemperatureChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel2.setStatus(_A)
_Zxr10OpticalSTemperatureChannel2Valid_Type=Integer32
_Zxr10OpticalSTemperatureChannel2Valid_Object=MibTableColumn
zxr10OpticalSTemperatureChannel2Valid=_Zxr10OpticalSTemperatureChannel2Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,61),_Zxr10OpticalSTemperatureChannel2Valid_Type())
zxr10OpticalSTemperatureChannel2Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel2Valid.setStatus(_A)
class _Zxr10OpticalSTemperatureChannel3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTemperatureChannel3_Type.__name__=_C
_Zxr10OpticalSTemperatureChannel3_Object=MibTableColumn
zxr10OpticalSTemperatureChannel3=_Zxr10OpticalSTemperatureChannel3_Object((1,3,6,1,4,1,3902,3,103,11,1,1,62),_Zxr10OpticalSTemperatureChannel3_Type())
zxr10OpticalSTemperatureChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel3.setStatus(_A)
_Zxr10OpticalSTemperatureChannel3Valid_Type=Integer32
_Zxr10OpticalSTemperatureChannel3Valid_Object=MibTableColumn
zxr10OpticalSTemperatureChannel3Valid=_Zxr10OpticalSTemperatureChannel3Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,63),_Zxr10OpticalSTemperatureChannel3Valid_Type())
zxr10OpticalSTemperatureChannel3Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel3Valid.setStatus(_A)
class _Zxr10OpticalSTemperatureChannel4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10OpticalSTemperatureChannel4_Type.__name__=_C
_Zxr10OpticalSTemperatureChannel4_Object=MibTableColumn
zxr10OpticalSTemperatureChannel4=_Zxr10OpticalSTemperatureChannel4_Object((1,3,6,1,4,1,3902,3,103,11,1,1,64),_Zxr10OpticalSTemperatureChannel4_Type())
zxr10OpticalSTemperatureChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel4.setStatus(_A)
_Zxr10OpticalSTemperatureChannel4Valid_Type=Integer32
_Zxr10OpticalSTemperatureChannel4Valid_Object=MibTableColumn
zxr10OpticalSTemperatureChannel4Valid=_Zxr10OpticalSTemperatureChannel4Valid_Object((1,3,6,1,4,1,3902,3,103,11,1,1,65),_Zxr10OpticalSTemperatureChannel4Valid_Type())
zxr10OpticalSTemperatureChannel4Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10OpticalSTemperatureChannel4Valid.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_C:DisplayString,'OpticalOnline':OpticalOnline,'SonetComplianceCodesType':SonetComplianceCodesType,'SonetComplianceCodesSpeed':SonetComplianceCodesSpeed,'GigabitEthernetComplianceCodesType':GigabitEthernetComplianceCodesType,'InfinibandComplianceCodesType':InfinibandComplianceCodesType,'GigabitEthernetComplianceCodesSpeed':GigabitEthernetComplianceCodesSpeed,'InfinibandComplianceCodesSpeed':InfinibandComplianceCodesSpeed,'zxr10OpticalMIB':zxr10OpticalMIB,'zxr10OpticalTable':zxr10OpticalTable,'zxr10OpticalEntry':zxr10OpticalEntry,_G:zxr10OpticalIfIndex,'zxr10OpticalIfName':zxr10OpticalIfName,'zxr10OpticalOnline':zxr10OpticalOnline,'zxr10OpticalFpType':zxr10OpticalFpType,'zxr10OpticalSonetComplianceCodesType':zxr10OpticalSonetComplianceCodesType,'zxr10OpticalSonetComplianceCodesSpeed':zxr10OpticalSonetComplianceCodesSpeed,'zxr10OpticalGigabitEthernetComplianceCodesType':zxr10OpticalGigabitEthernetComplianceCodesType,'zxr10OpticalGigabitEthernetComplianceCodesSpeed':zxr10OpticalGigabitEthernetComplianceCodesSpeed,'zxr10OpticalInfinibandComplianceCodesType':zxr10OpticalInfinibandComplianceCodesType,'zxr10OpticalInfinibandComplianceCodesSpeed':zxr10OpticalInfinibandComplianceCodesSpeed,'zxr10OpticalDisSMFkm':zxr10OpticalDisSMFkm,'zxr10OpticalDis9um':zxr10OpticalDis9um,'zxr10OpticalDis50um':zxr10OpticalDis50um,'zxr10OpticalDis62um':zxr10OpticalDis62um,'zxr10OpticalDiscopperLine':zxr10OpticalDiscopperLine,'zxr10OpticalSWaveLenth':zxr10OpticalSWaveLenth,'zxr10OpticalSWaveLenthValid':zxr10OpticalSWaveLenthValid,'zxr10OpticalSRxPower':zxr10OpticalSRxPower,'zxr10OpticalSRxPowerValid':zxr10OpticalSRxPowerValid,'zxr10OpticalSTxPower':zxr10OpticalSTxPower,'zxr10OpticalSTxPowerValid':zxr10OpticalSTxPowerValid,'zxr10OpticalSTxCurrent':zxr10OpticalSTxCurrent,'zxr10OpticalSTxCurrentValid':zxr10OpticalSTxCurrentValid,'zxr10OpticalSTemperature':zxr10OpticalSTemperature,'zxr10OpticalSTemperatureValid':zxr10OpticalSTemperatureValid,'zxr10Optical33SVoltage':zxr10Optical33SVoltage,'zxr10Optical33SVoltageValid':zxr10Optical33SVoltageValid,'zxr10Optical5SVoltage':zxr10Optical5SVoltage,'zxr10Optical5SVoltageValid':zxr10Optical5SVoltageValid,'zxr10OpticalVName':zxr10OpticalVName,'zxr10OpticalVPn':zxr10OpticalVPn,'zxr10OpticalRev':zxr10OpticalRev,'zxr10OpticalVSn':zxr10OpticalVSn,'zxr10OpticalSRxPowerChannel1':zxr10OpticalSRxPowerChannel1,'zxr10OpticalSRxPowerChannel1Valid':zxr10OpticalSRxPowerChannel1Valid,'zxr10OpticalSRxPowerChannel2':zxr10OpticalSRxPowerChannel2,'zxr10OpticalSRxPowerChannel2Valid':zxr10OpticalSRxPowerChannel2Valid,'zxr10OpticalSRxPowerChannel3':zxr10OpticalSRxPowerChannel3,'zxr10OpticalSRxPowerChannel3Valid':zxr10OpticalSRxPowerChannel3Valid,'zxr10OpticalSRxPowerChannel4':zxr10OpticalSRxPowerChannel4,'zxr10OpticalSRxPowerChannel4Valid':zxr10OpticalSRxPowerChannel4Valid,'zxr10OpticalSTxPowerChannel1':zxr10OpticalSTxPowerChannel1,'zxr10OpticalSTxPowerChannel1Valid':zxr10OpticalSTxPowerChannel1Valid,'zxr10OpticalSTxPowerChannel2':zxr10OpticalSTxPowerChannel2,'zxr10OpticalSTxPowerChannel2Valid':zxr10OpticalSTxPowerChannel2Valid,'zxr10OpticalSTxPowerChannel3':zxr10OpticalSTxPowerChannel3,'zxr10OpticalSTxPowerChannel3Valid':zxr10OpticalSTxPowerChannel3Valid,'zxr10OpticalSTxPowerChannel4':zxr10OpticalSTxPowerChannel4,'zxr10OpticalSTxPowerChannel4Valid':zxr10OpticalSTxPowerChannel4Valid,'zxr10OpticalSTxCurrentChannel1':zxr10OpticalSTxCurrentChannel1,'zxr10OpticalSTxCurrentChannel1Valid':zxr10OpticalSTxCurrentChannel1Valid,'zxr10OpticalSTxCurrentChannel2':zxr10OpticalSTxCurrentChannel2,'zxr10OpticalSTxCurrentChannel2Valid':zxr10OpticalSTxCurrentChannel2Valid,'zxr10OpticalSTxCurrentChannel3':zxr10OpticalSTxCurrentChannel3,'zxr10OpticalSTxCurrentChannel3Valid':zxr10OpticalSTxCurrentChannel3Valid,'zxr10OpticalSTxCurrentChannel4':zxr10OpticalSTxCurrentChannel4,'zxr10OpticalSTxCurrentChannel4Valid':zxr10OpticalSTxCurrentChannel4Valid,'zxr10OpticalSTemperatureChannel1':zxr10OpticalSTemperatureChannel1,'zxr10OpticalSTemperatureChannel1Valid':zxr10OpticalSTemperatureChannel1Valid,'zxr10OpticalSTemperatureChannel2':zxr10OpticalSTemperatureChannel2,'zxr10OpticalSTemperatureChannel2Valid':zxr10OpticalSTemperatureChannel2Valid,'zxr10OpticalSTemperatureChannel3':zxr10OpticalSTemperatureChannel3,'zxr10OpticalSTemperatureChannel3Valid':zxr10OpticalSTemperatureChannel3Valid,'zxr10OpticalSTemperatureChannel4':zxr10OpticalSTemperatureChannel4,'zxr10OpticalSTemperatureChannel4Valid':zxr10OpticalSTemperatureChannel4Valid})