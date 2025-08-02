_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hardwareNGOAWDevices,=mibBuilder.importSymbols('ALCATEL-NGOAW-BASE-MIB','hardwareNGOAWDevices')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelNGOAWDevicesMIB=ModuleIdentity((1,3,6,1,4,1,6486,802,1,1,2,1))
if mibBuilder.loadTexts:alcatelNGOAWDevicesMIB.setRevisions(('2016-09-01 00:00','2019-05-15 00:00','2019-08-26 00:00','2021-03-18 00:00','2022-03-10 00:00'))
_FamilyNGOAWWirelessSwitch_ObjectIdentity=ObjectIdentity
familyNGOAWWirelessSwitch=_FamilyNGOAWWirelessSwitch_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,1))
if mibBuilder.loadTexts:familyNGOAWWirelessSwitch.setStatus(_A)
_FamilyNGOAWWirelessAP_ObjectIdentity=ObjectIdentity
familyNGOAWWirelessAP=_FamilyNGOAWWirelessAP_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2))
if mibBuilder.loadTexts:familyNGOAWWirelessAP.setStatus(_A)
_DeviceNGOAWAp1101_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1101=_DeviceNGOAWAp1101_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,1))
if mibBuilder.loadTexts:deviceNGOAWAp1101.setStatus(_A)
_DeviceNGOAWAp1221_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1221=_DeviceNGOAWAp1221_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,2))
if mibBuilder.loadTexts:deviceNGOAWAp1221.setStatus(_A)
_DeviceNGOAWAp1222_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1222=_DeviceNGOAWAp1222_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,3))
if mibBuilder.loadTexts:deviceNGOAWAp1222.setStatus(_A)
_DeviceNGOAWAp1231_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1231=_DeviceNGOAWAp1231_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,4))
if mibBuilder.loadTexts:deviceNGOAWAp1231.setStatus(_A)
_DeviceNGOAWAp1232_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1232=_DeviceNGOAWAp1232_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,5))
if mibBuilder.loadTexts:deviceNGOAWAp1232.setStatus(_A)
_DeviceNGOAWAp1251_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1251=_DeviceNGOAWAp1251_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,6))
if mibBuilder.loadTexts:deviceNGOAWAp1251.setStatus(_A)
_DeviceNGOAWAp1251D_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1251D=_DeviceNGOAWAp1251D_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,7))
if mibBuilder.loadTexts:deviceNGOAWAp1251D.setStatus(_A)
_DeviceNGOAWAp1201H_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1201H=_DeviceNGOAWAp1201H_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,8))
if mibBuilder.loadTexts:deviceNGOAWAp1201H.setStatus(_A)
_DeviceNGOAWAp1201_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1201=_DeviceNGOAWAp1201_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,9))
if mibBuilder.loadTexts:deviceNGOAWAp1201.setStatus(_A)
_DeviceNGOAWAp1201L_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1201L=_DeviceNGOAWAp1201L_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,10))
if mibBuilder.loadTexts:deviceNGOAWAp1201L.setStatus(_A)
_DeviceNGOAWAp1201HL_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1201HL=_DeviceNGOAWAp1201HL_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,11))
if mibBuilder.loadTexts:deviceNGOAWAp1201HL.setStatus(_A)
_DeviceNGOAWAp1321_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1321=_DeviceNGOAWAp1321_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,12))
if mibBuilder.loadTexts:deviceNGOAWAp1321.setStatus(_A)
_DeviceNGOAWAp1322_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1322=_DeviceNGOAWAp1322_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,13))
if mibBuilder.loadTexts:deviceNGOAWAp1322.setStatus(_A)
_DeviceNGOAWAp1361_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1361=_DeviceNGOAWAp1361_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,14))
if mibBuilder.loadTexts:deviceNGOAWAp1361.setStatus(_A)
_DeviceNGOAWAp1361D_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1361D=_DeviceNGOAWAp1361D_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,15))
if mibBuilder.loadTexts:deviceNGOAWAp1361D.setStatus(_A)
_DeviceNGOAWAp1362_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1362=_DeviceNGOAWAp1362_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,16))
if mibBuilder.loadTexts:deviceNGOAWAp1362.setStatus(_A)
_DeviceNGOAWAp1201BG_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1201BG=_DeviceNGOAWAp1201BG_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,17))
if mibBuilder.loadTexts:deviceNGOAWAp1201BG.setStatus(_A)
_DeviceNGOAWAp1251RWB_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1251RWB=_DeviceNGOAWAp1251RWB_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,18))
if mibBuilder.loadTexts:deviceNGOAWAp1251RWB.setStatus(_A)
_DeviceNGOAWAp1301_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1301=_DeviceNGOAWAp1301_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,19))
if mibBuilder.loadTexts:deviceNGOAWAp1301.setStatus(_A)
_DeviceNGOAWAp1311_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1311=_DeviceNGOAWAp1311_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,20))
if mibBuilder.loadTexts:deviceNGOAWAp1311.setStatus(_A)
_DeviceNGOAWAp1341E_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1341E=_DeviceNGOAWAp1341E_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,21))
if mibBuilder.loadTexts:deviceNGOAWAp1341E.setStatus(_A)
_DeviceNGOAWAp1351_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1351=_DeviceNGOAWAp1351_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,22))
if mibBuilder.loadTexts:deviceNGOAWAp1351.setStatus(_A)
_DeviceNGOAWAp1331_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1331=_DeviceNGOAWAp1331_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,23))
if mibBuilder.loadTexts:deviceNGOAWAp1331.setStatus(_A)
_DeviceNGOAWAp1301H_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1301H=_DeviceNGOAWAp1301H_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,24))
if mibBuilder.loadTexts:deviceNGOAWAp1301H.setStatus(_A)
_DeviceNGOAWAp1261RWB_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1261RWB=_DeviceNGOAWAp1261RWB_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,25))
if mibBuilder.loadTexts:deviceNGOAWAp1261RWB.setStatus(_A)
_DeviceNGOAWAp1261_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1261=_DeviceNGOAWAp1261_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,26))
if mibBuilder.loadTexts:deviceNGOAWAp1261.setStatus(_A)
_DeviceNGOAWAp1451_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1451=_DeviceNGOAWAp1451_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,27))
if mibBuilder.loadTexts:deviceNGOAWAp1451.setStatus(_A)
_DeviceNGOAWAp1431_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1431=_DeviceNGOAWAp1431_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,28))
if mibBuilder.loadTexts:deviceNGOAWAp1431.setStatus(_A)
_DeviceNGOAWAp1362T_ObjectIdentity=ObjectIdentity
deviceNGOAWAp1362T=_DeviceNGOAWAp1362T_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2,1,2,29))
if mibBuilder.loadTexts:deviceNGOAWAp1362T.setStatus(_A)
mibBuilder.exportSymbols('ALCATEL-NGOAW-DEVICES-MIB',**{'alcatelNGOAWDevicesMIB':alcatelNGOAWDevicesMIB,'familyNGOAWWirelessSwitch':familyNGOAWWirelessSwitch,'familyNGOAWWirelessAP':familyNGOAWWirelessAP,'deviceNGOAWAp1101':deviceNGOAWAp1101,'deviceNGOAWAp1221':deviceNGOAWAp1221,'deviceNGOAWAp1222':deviceNGOAWAp1222,'deviceNGOAWAp1231':deviceNGOAWAp1231,'deviceNGOAWAp1232':deviceNGOAWAp1232,'deviceNGOAWAp1251':deviceNGOAWAp1251,'deviceNGOAWAp1251D':deviceNGOAWAp1251D,'deviceNGOAWAp1201H':deviceNGOAWAp1201H,'deviceNGOAWAp1201':deviceNGOAWAp1201,'deviceNGOAWAp1201L':deviceNGOAWAp1201L,'deviceNGOAWAp1201HL':deviceNGOAWAp1201HL,'deviceNGOAWAp1321':deviceNGOAWAp1321,'deviceNGOAWAp1322':deviceNGOAWAp1322,'deviceNGOAWAp1361':deviceNGOAWAp1361,'deviceNGOAWAp1361D':deviceNGOAWAp1361D,'deviceNGOAWAp1362':deviceNGOAWAp1362,'deviceNGOAWAp1201BG':deviceNGOAWAp1201BG,'deviceNGOAWAp1251RWB':deviceNGOAWAp1251RWB,'deviceNGOAWAp1301':deviceNGOAWAp1301,'deviceNGOAWAp1311':deviceNGOAWAp1311,'deviceNGOAWAp1341E':deviceNGOAWAp1341E,'deviceNGOAWAp1351':deviceNGOAWAp1351,'deviceNGOAWAp1331':deviceNGOAWAp1331,'deviceNGOAWAp1301H':deviceNGOAWAp1301H,'deviceNGOAWAp1261RWB':deviceNGOAWAp1261RWB,'deviceNGOAWAp1261':deviceNGOAWAp1261,'deviceNGOAWAp1451':deviceNGOAWAp1451,'deviceNGOAWAp1431':deviceNGOAWAp1431,'deviceNGOAWAp1362T':deviceNGOAWAp1362T})