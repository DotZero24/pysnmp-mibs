_J='enabled'
_I='disabled'
_H='activated'
_G='deactivated'
_F='DisplayString'
_E='OctetString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Trango_ObjectIdentity=ObjectIdentity
trango=_Trango_ObjectIdentity((1,3,6,1,4,1,5454))
_Tbw_ObjectIdentity=ObjectIdentity
tbw=_Tbw_ObjectIdentity((1,3,6,1,4,1,5454,1))
_P5830smu_ObjectIdentity=ObjectIdentity
p5830smu=_P5830smu_ObjectIdentity((1,3,6,1,4,1,5454,1,22))
_Musys_ObjectIdentity=ObjectIdentity
musys=_Musys_ObjectIdentity((1,3,6,1,4,1,5454,1,22,1))
_Muversion_ObjectIdentity=ObjectIdentity
muversion=_Muversion_ObjectIdentity((1,3,6,1,4,1,5454,1,22,1,1))
class _MuversionHW_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MuversionHW_Type.__name__=_E
_MuversionHW_Object=MibScalar
muversionHW=_MuversionHW_Object((1,3,6,1,4,1,5454,1,22,1,1,1),_MuversionHW_Type())
muversionHW.setMaxAccess(_D)
if mibBuilder.loadTexts:muversionHW.setStatus(_A)
class _MuversionFW_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_MuversionFW_Type.__name__=_F
_MuversionFW_Object=MibScalar
muversionFW=_MuversionFW_Object((1,3,6,1,4,1,5454,1,22,1,1,2),_MuversionFW_Type())
muversionFW.setMaxAccess(_D)
if mibBuilder.loadTexts:muversionFW.setStatus(_A)
class _MuversionFPGA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_MuversionFPGA_Type.__name__=_E
_MuversionFPGA_Object=MibScalar
muversionFPGA=_MuversionFPGA_Object((1,3,6,1,4,1,5454,1,22,1,1,3),_MuversionFPGA_Type())
muversionFPGA.setMaxAccess(_D)
if mibBuilder.loadTexts:muversionFPGA.setStatus(_A)
class _MuversionFWChecksum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_MuversionFWChecksum_Type.__name__=_E
_MuversionFWChecksum_Object=MibScalar
muversionFWChecksum=_MuversionFWChecksum_Object((1,3,6,1,4,1,5454,1,22,1,1,4),_MuversionFWChecksum_Type())
muversionFWChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:muversionFWChecksum.setStatus(_A)
class _MuversionFPGAChecksum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_MuversionFPGAChecksum_Type.__name__=_E
_MuversionFPGAChecksum_Object=MibScalar
muversionFPGAChecksum=_MuversionFPGAChecksum_Object((1,3,6,1,4,1,5454,1,22,1,1,5),_MuversionFPGAChecksum_Type())
muversionFPGAChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:muversionFPGAChecksum.setStatus(_A)
class _MusysDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_MusysDeviceId_Type.__name__=_E
_MusysDeviceId_Object=MibScalar
musysDeviceId=_MusysDeviceId_Object((1,3,6,1,4,1,5454,1,22,1,2),_MusysDeviceId_Type())
musysDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:musysDeviceId.setStatus(_A)
class _MusysDefOpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16)));namedValues=NamedValues(*(('off',0),('on',16)))
_MusysDefOpMode_Type.__name__=_B
_MusysDefOpMode_Object=MibScalar
musysDefOpMode=_MusysDefOpMode_Object((1,3,6,1,4,1,5454,1,22,1,3),_MusysDefOpMode_Type())
musysDefOpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:musysDefOpMode.setStatus(_A)
class _MusysCurOpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16)));namedValues=NamedValues(*(('off',0),('on',16)))
_MusysCurOpMode_Type.__name__=_B
_MusysCurOpMode_Object=MibScalar
musysCurOpMode=_MusysCurOpMode_Object((1,3,6,1,4,1,5454,1,22,1,4),_MusysCurOpMode_Type())
musysCurOpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:musysCurOpMode.setStatus(_A)
class _MusysActivateOpmode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_MusysActivateOpmode_Type.__name__=_B
_MusysActivateOpmode_Object=MibScalar
musysActivateOpmode=_MusysActivateOpmode_Object((1,3,6,1,4,1,5454,1,22,1,5),_MusysActivateOpmode_Type())
musysActivateOpmode.setMaxAccess(_C)
if mibBuilder.loadTexts:musysActivateOpmode.setStatus(_A)
class _MusysReadCommStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MusysReadCommStr_Type.__name__=_F
_MusysReadCommStr_Object=MibScalar
musysReadCommStr=_MusysReadCommStr_Object((1,3,6,1,4,1,5454,1,22,1,6),_MusysReadCommStr_Type())
musysReadCommStr.setMaxAccess(_C)
if mibBuilder.loadTexts:musysReadCommStr.setStatus(_A)
class _MusysWriteCommStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MusysWriteCommStr_Type.__name__=_F
_MusysWriteCommStr_Object=MibScalar
musysWriteCommStr=_MusysWriteCommStr_Object((1,3,6,1,4,1,5454,1,22,1,7),_MusysWriteCommStr_Type())
musysWriteCommStr.setMaxAccess(_C)
if mibBuilder.loadTexts:musysWriteCommStr.setStatus(_A)
_Muswitches_ObjectIdentity=ObjectIdentity
muswitches=_Muswitches_ObjectIdentity((1,3,6,1,4,1,5454,1,22,1,8))
class _MuswitchesBlockBroadcastMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('passed',0),('blocked',1)))
_MuswitchesBlockBroadcastMulticast_Type.__name__=_B
_MuswitchesBlockBroadcastMulticast_Object=MibScalar
muswitchesBlockBroadcastMulticast=_MuswitchesBlockBroadcastMulticast_Object((1,3,6,1,4,1,5454,1,22,1,8,1),_MuswitchesBlockBroadcastMulticast_Type())
muswitchesBlockBroadcastMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:muswitchesBlockBroadcastMulticast.setStatus(_A)
class _MuswitchesHTTPD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MuswitchesHTTPD_Type.__name__=_B
_MuswitchesHTTPD_Object=MibScalar
muswitchesHTTPD=_MuswitchesHTTPD_Object((1,3,6,1,4,1,5454,1,22,1,8,5),_MuswitchesHTTPD_Type())
muswitchesHTTPD.setMaxAccess(_C)
if mibBuilder.loadTexts:muswitchesHTTPD.setStatus(_A)
class _MuswitchesAutoPowerLevelRemoteUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MuswitchesAutoPowerLevelRemoteUnit_Type.__name__=_B
_MuswitchesAutoPowerLevelRemoteUnit_Object=MibScalar
muswitchesAutoPowerLevelRemoteUnit=_MuswitchesAutoPowerLevelRemoteUnit_Object((1,3,6,1,4,1,5454,1,22,1,8,7),_MuswitchesAutoPowerLevelRemoteUnit_Type())
muswitchesAutoPowerLevelRemoteUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:muswitchesAutoPowerLevelRemoteUnit.setStatus(_A)
_Mutraffic_ObjectIdentity=ObjectIdentity
mutraffic=_Mutraffic_ObjectIdentity((1,3,6,1,4,1,5454,1,22,1,9))
_MutrafficEthInOctets_Type=Counter32
_MutrafficEthInOctets_Object=MibScalar
mutrafficEthInOctets=_MutrafficEthInOctets_Object((1,3,6,1,4,1,5454,1,22,1,9,1),_MutrafficEthInOctets_Type())
mutrafficEthInOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mutrafficEthInOctets.setStatus(_A)
_MutrafficEthOutOctets_Type=Counter32
_MutrafficEthOutOctets_Object=MibScalar
mutrafficEthOutOctets=_MutrafficEthOutOctets_Object((1,3,6,1,4,1,5454,1,22,1,9,2),_MutrafficEthOutOctets_Type())
mutrafficEthOutOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mutrafficEthOutOctets.setStatus(_A)
_MutrafficRfInOctets_Type=Counter32
_MutrafficRfInOctets_Object=MibScalar
mutrafficRfInOctets=_MutrafficRfInOctets_Object((1,3,6,1,4,1,5454,1,22,1,9,3),_MutrafficRfInOctets_Type())
mutrafficRfInOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mutrafficRfInOctets.setStatus(_A)
_MutrafficRfOutOctets_Type=Counter32
_MutrafficRfOutOctets_Object=MibScalar
mutrafficRfOutOctets=_MutrafficRfOutOctets_Object((1,3,6,1,4,1,5454,1,22,1,9,4),_MutrafficRfOutOctets_Type())
mutrafficRfOutOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mutrafficRfOutOctets.setStatus(_A)
class _MusysTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MusysTemperature_Type.__name__=_B
_MusysTemperature_Object=MibScalar
musysTemperature=_MusysTemperature_Object((1,3,6,1,4,1,5454,1,22,1,10),_MusysTemperature_Type())
musysTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:musysTemperature.setStatus(_A)
class _MusysUpdateFlashAndActivate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_MusysUpdateFlashAndActivate_Type.__name__=_B
_MusysUpdateFlashAndActivate_Object=MibScalar
musysUpdateFlashAndActivate=_MusysUpdateFlashAndActivate_Object((1,3,6,1,4,1,5454,1,22,1,11),_MusysUpdateFlashAndActivate_Type())
musysUpdateFlashAndActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:musysUpdateFlashAndActivate.setStatus(_A)
class _MusysReboot_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_MusysReboot_Type.__name__=_B
_MusysReboot_Object=MibScalar
musysReboot=_MusysReboot_Object((1,3,6,1,4,1,5454,1,22,1,12),_MusysReboot_Type())
musysReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:musysReboot.setStatus(_A)
_Muipconfig_ObjectIdentity=ObjectIdentity
muipconfig=_Muipconfig_ObjectIdentity((1,3,6,1,4,1,5454,1,22,1,13))
_MuipconfigIpAddress_Type=IpAddress
_MuipconfigIpAddress_Object=MibScalar
muipconfigIpAddress=_MuipconfigIpAddress_Object((1,3,6,1,4,1,5454,1,22,1,13,1),_MuipconfigIpAddress_Type())
muipconfigIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:muipconfigIpAddress.setStatus(_A)
_MuipconfigSubnet_Type=IpAddress
_MuipconfigSubnet_Object=MibScalar
muipconfigSubnet=_MuipconfigSubnet_Object((1,3,6,1,4,1,5454,1,22,1,13,2),_MuipconfigSubnet_Type())
muipconfigSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:muipconfigSubnet.setStatus(_A)
_MuipconfigDefaultGateway_Type=IpAddress
_MuipconfigDefaultGateway_Object=MibScalar
muipconfigDefaultGateway=_MuipconfigDefaultGateway_Object((1,3,6,1,4,1,5454,1,22,1,13,3),_MuipconfigDefaultGateway_Type())
muipconfigDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:muipconfigDefaultGateway.setStatus(_A)
_Murf_ObjectIdentity=ObjectIdentity
murf=_Murf_ObjectIdentity((1,3,6,1,4,1,5454,1,22,2))
class _MurfRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MurfRSSI_Type.__name__=_B
_MurfRSSI_Object=MibScalar
murfRSSI=_MurfRSSI_Object((1,3,6,1,4,1,5454,1,22,2,1),_MurfRSSI_Type())
murfRSSI.setMaxAccess(_D)
if mibBuilder.loadTexts:murfRSSI.setStatus(_A)
class _MurfActiveChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_MurfActiveChannel_Type.__name__=_B
_MurfActiveChannel_Object=MibScalar
murfActiveChannel=_MurfActiveChannel_Object((1,3,6,1,4,1,5454,1,22,2,2),_MurfActiveChannel_Type())
murfActiveChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:murfActiveChannel.setStatus(_A)
class _MurfActivePolarization_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_MurfActivePolarization_Type.__name__=_F
_MurfActivePolarization_Object=MibScalar
murfActivePolarization=_MurfActivePolarization_Object((1,3,6,1,4,1,5454,1,22,2,3),_MurfActivePolarization_Type())
murfActivePolarization.setMaxAccess(_C)
if mibBuilder.loadTexts:murfActivePolarization.setStatus(_A)
_Murftable_ObjectIdentity=ObjectIdentity
murftable=_Murftable_ObjectIdentity((1,3,6,1,4,1,5454,1,22,2,4))
class _MurftableChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel1_Type.__name__=_B
_MurftableChannel1_Object=MibScalar
murftableChannel1=_MurftableChannel1_Object((1,3,6,1,4,1,5454,1,22,2,4,1),_MurftableChannel1_Type())
murftableChannel1.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel1.setStatus(_A)
class _MurftableChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel2_Type.__name__=_B
_MurftableChannel2_Object=MibScalar
murftableChannel2=_MurftableChannel2_Object((1,3,6,1,4,1,5454,1,22,2,4,2),_MurftableChannel2_Type())
murftableChannel2.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel2.setStatus(_A)
class _MurftableChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel3_Type.__name__=_B
_MurftableChannel3_Object=MibScalar
murftableChannel3=_MurftableChannel3_Object((1,3,6,1,4,1,5454,1,22,2,4,3),_MurftableChannel3_Type())
murftableChannel3.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel3.setStatus(_A)
class _MurftableChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel4_Type.__name__=_B
_MurftableChannel4_Object=MibScalar
murftableChannel4=_MurftableChannel4_Object((1,3,6,1,4,1,5454,1,22,2,4,4),_MurftableChannel4_Type())
murftableChannel4.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel4.setStatus(_A)
class _MurftableChannel5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel5_Type.__name__=_B
_MurftableChannel5_Object=MibScalar
murftableChannel5=_MurftableChannel5_Object((1,3,6,1,4,1,5454,1,22,2,4,5),_MurftableChannel5_Type())
murftableChannel5.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel5.setStatus(_A)
class _MurftableChannel6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel6_Type.__name__=_B
_MurftableChannel6_Object=MibScalar
murftableChannel6=_MurftableChannel6_Object((1,3,6,1,4,1,5454,1,22,2,4,6),_MurftableChannel6_Type())
murftableChannel6.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel6.setStatus(_A)
class _MurftableChannel7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel7_Type.__name__=_B
_MurftableChannel7_Object=MibScalar
murftableChannel7=_MurftableChannel7_Object((1,3,6,1,4,1,5454,1,22,2,4,7),_MurftableChannel7_Type())
murftableChannel7.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel7.setStatus(_A)
class _MurftableChannel8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel8_Type.__name__=_B
_MurftableChannel8_Object=MibScalar
murftableChannel8=_MurftableChannel8_Object((1,3,6,1,4,1,5454,1,22,2,4,8),_MurftableChannel8_Type())
murftableChannel8.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel8.setStatus(_A)
class _MurftableChannel9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel9_Type.__name__=_B
_MurftableChannel9_Object=MibScalar
murftableChannel9=_MurftableChannel9_Object((1,3,6,1,4,1,5454,1,22,2,4,9),_MurftableChannel9_Type())
murftableChannel9.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel9.setStatus(_A)
class _MurftableChannel10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel10_Type.__name__=_B
_MurftableChannel10_Object=MibScalar
murftableChannel10=_MurftableChannel10_Object((1,3,6,1,4,1,5454,1,22,2,4,10),_MurftableChannel10_Type())
murftableChannel10.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel10.setStatus(_A)
class _MurftableChannel11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel11_Type.__name__=_B
_MurftableChannel11_Object=MibScalar
murftableChannel11=_MurftableChannel11_Object((1,3,6,1,4,1,5454,1,22,2,4,11),_MurftableChannel11_Type())
murftableChannel11.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel11.setStatus(_A)
class _MurftableChannel12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel12_Type.__name__=_B
_MurftableChannel12_Object=MibScalar
murftableChannel12=_MurftableChannel12_Object((1,3,6,1,4,1,5454,1,22,2,4,12),_MurftableChannel12_Type())
murftableChannel12.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel12.setStatus(_A)
class _MurftableChannel13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel13_Type.__name__=_B
_MurftableChannel13_Object=MibScalar
murftableChannel13=_MurftableChannel13_Object((1,3,6,1,4,1,5454,1,22,2,4,13),_MurftableChannel13_Type())
murftableChannel13.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel13.setStatus(_A)
class _MurftableChannel14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel14_Type.__name__=_B
_MurftableChannel14_Object=MibScalar
murftableChannel14=_MurftableChannel14_Object((1,3,6,1,4,1,5454,1,22,2,4,14),_MurftableChannel14_Type())
murftableChannel14.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel14.setStatus(_A)
class _MurftableChannel15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel15_Type.__name__=_B
_MurftableChannel15_Object=MibScalar
murftableChannel15=_MurftableChannel15_Object((1,3,6,1,4,1,5454,1,22,2,4,15),_MurftableChannel15_Type())
murftableChannel15.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel15.setStatus(_A)
class _MurftableChannel16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel16_Type.__name__=_B
_MurftableChannel16_Object=MibScalar
murftableChannel16=_MurftableChannel16_Object((1,3,6,1,4,1,5454,1,22,2,4,16),_MurftableChannel16_Type())
murftableChannel16.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel16.setStatus(_A)
class _MurftableChannel17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel17_Type.__name__=_B
_MurftableChannel17_Object=MibScalar
murftableChannel17=_MurftableChannel17_Object((1,3,6,1,4,1,5454,1,22,2,4,17),_MurftableChannel17_Type())
murftableChannel17.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel17.setStatus(_A)
class _MurftableChannel18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel18_Type.__name__=_B
_MurftableChannel18_Object=MibScalar
murftableChannel18=_MurftableChannel18_Object((1,3,6,1,4,1,5454,1,22,2,4,18),_MurftableChannel18_Type())
murftableChannel18.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel18.setStatus(_A)
class _MurftableChannel19_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel19_Type.__name__=_B
_MurftableChannel19_Object=MibScalar
murftableChannel19=_MurftableChannel19_Object((1,3,6,1,4,1,5454,1,22,2,4,19),_MurftableChannel19_Type())
murftableChannel19.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel19.setStatus(_A)
class _MurftableChannel20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel20_Type.__name__=_B
_MurftableChannel20_Object=MibScalar
murftableChannel20=_MurftableChannel20_Object((1,3,6,1,4,1,5454,1,22,2,4,20),_MurftableChannel20_Type())
murftableChannel20.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel20.setStatus(_A)
class _MurftableChannel21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel21_Type.__name__=_B
_MurftableChannel21_Object=MibScalar
murftableChannel21=_MurftableChannel21_Object((1,3,6,1,4,1,5454,1,22,2,4,21),_MurftableChannel21_Type())
murftableChannel21.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel21.setStatus(_A)
class _MurftableChannel22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel22_Type.__name__=_B
_MurftableChannel22_Object=MibScalar
murftableChannel22=_MurftableChannel22_Object((1,3,6,1,4,1,5454,1,22,2,4,22),_MurftableChannel22_Type())
murftableChannel22.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel22.setStatus(_A)
class _MurftableChannel23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel23_Type.__name__=_B
_MurftableChannel23_Object=MibScalar
murftableChannel23=_MurftableChannel23_Object((1,3,6,1,4,1,5454,1,22,2,4,23),_MurftableChannel23_Type())
murftableChannel23.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel23.setStatus(_A)
class _MurftableChannel24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel24_Type.__name__=_B
_MurftableChannel24_Object=MibScalar
murftableChannel24=_MurftableChannel24_Object((1,3,6,1,4,1,5454,1,22,2,4,24),_MurftableChannel24_Type())
murftableChannel24.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel24.setStatus(_A)
class _MurftableChannel25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel25_Type.__name__=_B
_MurftableChannel25_Object=MibScalar
murftableChannel25=_MurftableChannel25_Object((1,3,6,1,4,1,5454,1,22,2,4,25),_MurftableChannel25_Type())
murftableChannel25.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel25.setStatus(_A)
class _MurftableChannel26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel26_Type.__name__=_B
_MurftableChannel26_Object=MibScalar
murftableChannel26=_MurftableChannel26_Object((1,3,6,1,4,1,5454,1,22,2,4,26),_MurftableChannel26_Type())
murftableChannel26.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel26.setStatus(_A)
class _MurftableChannel27_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel27_Type.__name__=_B
_MurftableChannel27_Object=MibScalar
murftableChannel27=_MurftableChannel27_Object((1,3,6,1,4,1,5454,1,22,2,4,27),_MurftableChannel27_Type())
murftableChannel27.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel27.setStatus(_A)
class _MurftableChannel28_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel28_Type.__name__=_B
_MurftableChannel28_Object=MibScalar
murftableChannel28=_MurftableChannel28_Object((1,3,6,1,4,1,5454,1,22,2,4,28),_MurftableChannel28_Type())
murftableChannel28.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel28.setStatus(_A)
class _MurftableChannel29_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel29_Type.__name__=_B
_MurftableChannel29_Object=MibScalar
murftableChannel29=_MurftableChannel29_Object((1,3,6,1,4,1,5454,1,22,2,4,29),_MurftableChannel29_Type())
murftableChannel29.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel29.setStatus(_A)
class _MurftableChannel30_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5260,5340),ValueRangeConstraint(5736,5836))
_MurftableChannel30_Type.__name__=_B
_MurftableChannel30_Object=MibScalar
murftableChannel30=_MurftableChannel30_Object((1,3,6,1,4,1,5454,1,22,2,4,30),_MurftableChannel30_Type())
murftableChannel30.setMaxAccess(_C)
if mibBuilder.loadTexts:murftableChannel30.setStatus(_A)
_Muism_ObjectIdentity=ObjectIdentity
muism=_Muism_ObjectIdentity((1,3,6,1,4,1,5454,1,22,2,5))
class _MuismTxPowerMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MuismTxPowerMax_Type.__name__=_B
_MuismTxPowerMax_Object=MibScalar
muismTxPowerMax=_MuismTxPowerMax_Object((1,3,6,1,4,1,5454,1,22,2,5,1),_MuismTxPowerMax_Type())
muismTxPowerMax.setMaxAccess(_D)
if mibBuilder.loadTexts:muismTxPowerMax.setStatus(_A)
class _MuismTxPowerMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MuismTxPowerMin_Type.__name__=_B
_MuismTxPowerMin_Object=MibScalar
muismTxPowerMin=_MuismTxPowerMin_Object((1,3,6,1,4,1,5454,1,22,2,5,2),_MuismTxPowerMin_Type())
muismTxPowerMin.setMaxAccess(_D)
if mibBuilder.loadTexts:muismTxPowerMin.setStatus(_A)
class _MuismTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MuismTxPower_Type.__name__=_B
_MuismTxPower_Object=MibScalar
muismTxPower=_MuismTxPower_Object((1,3,6,1,4,1,5454,1,22,2,5,3),_MuismTxPower_Type())
muismTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:muismTxPower.setStatus(_A)
class _MuismRxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-90,-90),ValueRangeConstraint(-85,-85),ValueRangeConstraint(-80,-80),ValueRangeConstraint(-75,-75),ValueRangeConstraint(-70,-70),ValueRangeConstraint(-65,-65))
_MuismRxThreshold_Type.__name__=_B
_MuismRxThreshold_Object=MibScalar
muismRxThreshold=_MuismRxThreshold_Object((1,3,6,1,4,1,5454,1,22,2,5,4),_MuismRxThreshold_Type())
muismRxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:muismRxThreshold.setStatus(_A)
class _MuismTargetRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-85,-45))
_MuismTargetRSSI_Type.__name__=_B
_MuismTargetRSSI_Object=MibScalar
muismTargetRSSI=_MuismTargetRSSI_Object((1,3,6,1,4,1,5454,1,22,2,5,5),_MuismTargetRSSI_Type())
muismTargetRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:muismTargetRSSI.setStatus(_A)
_Muunii_ObjectIdentity=ObjectIdentity
muunii=_Muunii_ObjectIdentity((1,3,6,1,4,1,5454,1,22,2,6))
class _MuuniiTxPowerMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MuuniiTxPowerMax_Type.__name__=_B
_MuuniiTxPowerMax_Object=MibScalar
muuniiTxPowerMax=_MuuniiTxPowerMax_Object((1,3,6,1,4,1,5454,1,22,2,6,1),_MuuniiTxPowerMax_Type())
muuniiTxPowerMax.setMaxAccess(_D)
if mibBuilder.loadTexts:muuniiTxPowerMax.setStatus(_A)
class _MuuniiTxPowerMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MuuniiTxPowerMin_Type.__name__=_B
_MuuniiTxPowerMin_Object=MibScalar
muuniiTxPowerMin=_MuuniiTxPowerMin_Object((1,3,6,1,4,1,5454,1,22,2,6,2),_MuuniiTxPowerMin_Type())
muuniiTxPowerMin.setMaxAccess(_D)
if mibBuilder.loadTexts:muuniiTxPowerMin.setStatus(_A)
class _MuuniiTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_MuuniiTxPower_Type.__name__=_B
_MuuniiTxPower_Object=MibScalar
muuniiTxPower=_MuuniiTxPower_Object((1,3,6,1,4,1,5454,1,22,2,6,3),_MuuniiTxPower_Type())
muuniiTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:muuniiTxPower.setStatus(_A)
class _MuuniiRxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-90,-90),ValueRangeConstraint(-85,-85),ValueRangeConstraint(-80,-80),ValueRangeConstraint(-75,-75),ValueRangeConstraint(-70,-70),ValueRangeConstraint(-65,-65))
_MuuniiRxThreshold_Type.__name__=_B
_MuuniiRxThreshold_Object=MibScalar
muuniiRxThreshold=_MuuniiRxThreshold_Object((1,3,6,1,4,1,5454,1,22,2,6,4),_MuuniiRxThreshold_Type())
muuniiRxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:muuniiRxThreshold.setStatus(_A)
class _MuuniiTargetRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-85,-45))
_MuuniiTargetRSSI_Type.__name__=_B
_MuuniiTargetRSSI_Object=MibScalar
muuniiTargetRSSI=_MuuniiTargetRSSI_Object((1,3,6,1,4,1,5454,1,22,2,6,5),_MuuniiTargetRSSI_Type())
muuniiTargetRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:muuniiTargetRSSI.setStatus(_A)
_Ru_ObjectIdentity=ObjectIdentity
ru=_Ru_ObjectIdentity((1,3,6,1,4,1,5454,1,22,3))
class _RuDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_RuDeviceId_Type.__name__=_E
_RuDeviceId_Object=MibScalar
ruDeviceId=_RuDeviceId_Object((1,3,6,1,4,1,5454,1,22,3,1),_RuDeviceId_Type())
ruDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:ruDeviceId.setStatus(_A)
class _RuUpstreamMIR_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_RuUpstreamMIR_Type.__name__=_B
_RuUpstreamMIR_Object=MibScalar
ruUpstreamMIR=_RuUpstreamMIR_Object((1,3,6,1,4,1,5454,1,22,3,2),_RuUpstreamMIR_Type())
ruUpstreamMIR.setMaxAccess(_C)
if mibBuilder.loadTexts:ruUpstreamMIR.setStatus(_A)
class _RemoteDownstreamMIR_Type(Integer32):defaultValue=9999;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_RemoteDownstreamMIR_Type.__name__=_B
_RemoteDownstreamMIR_Object=MibScalar
remoteDownstreamMIR=_RemoteDownstreamMIR_Object((1,3,6,1,4,1,5454,1,22,3,3),_RemoteDownstreamMIR_Type())
remoteDownstreamMIR.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteDownstreamMIR.setStatus(_A)
class _RuPowerLvl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RuPowerLvl_Type.__name__=_B
_RuPowerLvl_Object=MibScalar
ruPowerLvl=_RuPowerLvl_Object((1,3,6,1,4,1,5454,1,22,3,4),_RuPowerLvl_Type())
ruPowerLvl.setMaxAccess(_C)
if mibBuilder.loadTexts:ruPowerLvl.setStatus(_A)
class _RuReboot_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_RuReboot_Type.__name__=_B
_RuReboot_Object=MibScalar
ruReboot=_RuReboot_Object((1,3,6,1,4,1,5454,1,22,3,5),_RuReboot_Type())
ruReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:ruReboot.setStatus(_A)
class _RuAssociation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notAssociated',0),('associated',1)))
_RuAssociation_Type.__name__=_B
_RuAssociation_Object=MibScalar
ruAssociation=_RuAssociation_Object((1,3,6,1,4,1,5454,1,22,3,6),_RuAssociation_Type())
ruAssociation.setMaxAccess(_D)
if mibBuilder.loadTexts:ruAssociation.setStatus(_A)
class _RuDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_RuDistance_Type.__name__=_B
_RuDistance_Object=MibScalar
ruDistance=_RuDistance_Object((1,3,6,1,4,1,5454,1,22,3,7),_RuDistance_Type())
ruDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:ruDistance.setStatus(_A)
_Trapconfig_ObjectIdentity=ObjectIdentity
trapconfig=_Trapconfig_ObjectIdentity((1,3,6,1,4,1,5454,1,22,4))
_TrapconfigDest1IPAddress_Type=IpAddress
_TrapconfigDest1IPAddress_Object=MibScalar
trapconfigDest1IPAddress=_TrapconfigDest1IPAddress_Object((1,3,6,1,4,1,5454,1,22,4,2),_TrapconfigDest1IPAddress_Type())
trapconfigDest1IPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trapconfigDest1IPAddress.setStatus(_A)
_TrapconfigDest2IPAddress_Type=IpAddress
_TrapconfigDest2IPAddress_Object=MibScalar
trapconfigDest2IPAddress=_TrapconfigDest2IPAddress_Object((1,3,6,1,4,1,5454,1,22,4,3),_TrapconfigDest2IPAddress_Type())
trapconfigDest2IPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trapconfigDest2IPAddress.setStatus(_A)
_Mibinfo_ObjectIdentity=ObjectIdentity
mibinfo=_Mibinfo_ObjectIdentity((1,3,6,1,4,1,5454,1,22,5))
class _MibinfoVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MibinfoVersion_Type.__name__=_F
_MibinfoVersion_Object=MibScalar
mibinfoVersion=_MibinfoVersion_Object((1,3,6,1,4,1,5454,1,22,5,1),_MibinfoVersion_Type())
mibinfoVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:mibinfoVersion.setStatus(_A)
mibBuilder.exportSymbols('TRANGOP5830S-MU-MIB',**{_F:DisplayString,'trango':trango,'tbw':tbw,'p5830smu':p5830smu,'musys':musys,'muversion':muversion,'muversionHW':muversionHW,'muversionFW':muversionFW,'muversionFPGA':muversionFPGA,'muversionFWChecksum':muversionFWChecksum,'muversionFPGAChecksum':muversionFPGAChecksum,'musysDeviceId':musysDeviceId,'musysDefOpMode':musysDefOpMode,'musysCurOpMode':musysCurOpMode,'musysActivateOpmode':musysActivateOpmode,'musysReadCommStr':musysReadCommStr,'musysWriteCommStr':musysWriteCommStr,'muswitches':muswitches,'muswitchesBlockBroadcastMulticast':muswitchesBlockBroadcastMulticast,'muswitchesHTTPD':muswitchesHTTPD,'muswitchesAutoPowerLevelRemoteUnit':muswitchesAutoPowerLevelRemoteUnit,'mutraffic':mutraffic,'mutrafficEthInOctets':mutrafficEthInOctets,'mutrafficEthOutOctets':mutrafficEthOutOctets,'mutrafficRfInOctets':mutrafficRfInOctets,'mutrafficRfOutOctets':mutrafficRfOutOctets,'musysTemperature':musysTemperature,'musysUpdateFlashAndActivate':musysUpdateFlashAndActivate,'musysReboot':musysReboot,'muipconfig':muipconfig,'muipconfigIpAddress':muipconfigIpAddress,'muipconfigSubnet':muipconfigSubnet,'muipconfigDefaultGateway':muipconfigDefaultGateway,'murf':murf,'murfRSSI':murfRSSI,'murfActiveChannel':murfActiveChannel,'murfActivePolarization':murfActivePolarization,'murftable':murftable,'murftableChannel1':murftableChannel1,'murftableChannel2':murftableChannel2,'murftableChannel3':murftableChannel3,'murftableChannel4':murftableChannel4,'murftableChannel5':murftableChannel5,'murftableChannel6':murftableChannel6,'murftableChannel7':murftableChannel7,'murftableChannel8':murftableChannel8,'murftableChannel9':murftableChannel9,'murftableChannel10':murftableChannel10,'murftableChannel11':murftableChannel11,'murftableChannel12':murftableChannel12,'murftableChannel13':murftableChannel13,'murftableChannel14':murftableChannel14,'murftableChannel15':murftableChannel15,'murftableChannel16':murftableChannel16,'murftableChannel17':murftableChannel17,'murftableChannel18':murftableChannel18,'murftableChannel19':murftableChannel19,'murftableChannel20':murftableChannel20,'murftableChannel21':murftableChannel21,'murftableChannel22':murftableChannel22,'murftableChannel23':murftableChannel23,'murftableChannel24':murftableChannel24,'murftableChannel25':murftableChannel25,'murftableChannel26':murftableChannel26,'murftableChannel27':murftableChannel27,'murftableChannel28':murftableChannel28,'murftableChannel29':murftableChannel29,'murftableChannel30':murftableChannel30,'muism':muism,'muismTxPowerMax':muismTxPowerMax,'muismTxPowerMin':muismTxPowerMin,'muismTxPower':muismTxPower,'muismRxThreshold':muismRxThreshold,'muismTargetRSSI':muismTargetRSSI,'muunii':muunii,'muuniiTxPowerMax':muuniiTxPowerMax,'muuniiTxPowerMin':muuniiTxPowerMin,'muuniiTxPower':muuniiTxPower,'muuniiRxThreshold':muuniiRxThreshold,'muuniiTargetRSSI':muuniiTargetRSSI,'ru':ru,'ruDeviceId':ruDeviceId,'ruUpstreamMIR':ruUpstreamMIR,'remoteDownstreamMIR':remoteDownstreamMIR,'ruPowerLvl':ruPowerLvl,'ruReboot':ruReboot,'ruAssociation':ruAssociation,'ruDistance':ruDistance,'trapconfig':trapconfig,'trapconfigDest1IPAddress':trapconfigDest1IPAddress,'trapconfigDest2IPAddress':trapconfigDest2IPAddress,'mibinfo':mibinfo,'mibinfoVersion':mibinfoVersion})