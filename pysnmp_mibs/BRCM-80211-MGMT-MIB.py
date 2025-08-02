_d='dot11BssAccessIndex'
_c='dot11BssWep128BitKeyIndex'
_b='dot11BssWep64BitKeyIndex'
_a='dot11AccessIndex'
_Z='denyList'
_Y='allowList'
_X='allowAny'
_W='disabled'
_V='dot11128BitKeyIndex'
_U='dot1164BitKeyIndex'
_T='tkipPlusAes'
_S='wep128'
_R='milliseconds'
_Q='2007-09-10 00:00'
_P='TruthValue'
_O='seconds'
_N='off'
_M='DisplayString'
_L='auto'
_K='not-accessible'
_J='read-create'
_I='BRCM-80211-MGMT-MIB'
_H='ifIndex'
_G='IF-MIB'
_F='Unsigned32'
_E='OctetString'
_D='deprecated'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtMIBObjects')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'MacAddress','PhysAddress','RowStatus','TextualConvention',_P)
ieee802dot11Mgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,5))
if mibBuilder.loadTexts:ieee802dot11Mgmt.setRevisions(('2009-01-12 00:00','2008-06-27 00:00',_Q,_Q,'2007-07-29 00:00','2007-03-01 00:00','2007-02-05 00:00','2004-08-11 00:00','2003-11-20 00:00','2003-08-20 00:00','2003-08-05 00:00','2003-04-16 00:00','2003-03-06 00:00'))
_Dot11MgmtBase_ObjectIdentity=ObjectIdentity
dot11MgmtBase=_Dot11MgmtBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,5,1))
class _Dot11OperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notAvailable',0),(_N,1),('remote',2),('local',3)))
_Dot11OperMode_Type.__name__=_C
_Dot11OperMode_Object=MibScalar
dot11OperMode=_Dot11OperMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,1),_Dot11OperMode_Type())
dot11OperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11OperMode.setStatus(_A)
class _Dot11SSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot11SSID_Type.__name__=_E
_Dot11SSID_Object=MibScalar
dot11SSID=_Dot11SSID_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,2),_Dot11SSID_Type())
dot11SSID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11SSID.setStatus(_D)
class _Dot11CurrentChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216))
_Dot11CurrentChannel_Type.__name__=_F
_Dot11CurrentChannel_Object=MibScalar
dot11CurrentChannel=_Dot11CurrentChannel_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,3),_Dot11CurrentChannel_Type())
dot11CurrentChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11CurrentChannel.setStatus(_A)
class _Dot11BeaconInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot11BeaconInterval_Type.__name__=_F
_Dot11BeaconInterval_Object=MibScalar
dot11BeaconInterval=_Dot11BeaconInterval_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,4),_Dot11BeaconInterval_Type())
dot11BeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:dot11BeaconInterval.setUnits(_R)
class _Dot11DTIMInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11DTIMInterval_Type.__name__=_F
_Dot11DTIMInterval_Object=MibScalar
dot11DTIMInterval=_Dot11DTIMInterval_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,5),_Dot11DTIMInterval_Type())
dot11DTIMInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DTIMInterval.setStatus(_A)
if mibBuilder.loadTexts:dot11DTIMInterval.setUnits(_R)
class _Dot11FragThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_Dot11FragThresh_Type.__name__=_F
_Dot11FragThresh_Object=MibScalar
dot11FragThresh=_Dot11FragThresh_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,6),_Dot11FragThresh_Type())
dot11FragThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FragThresh.setStatus(_A)
if mibBuilder.loadTexts:dot11FragThresh.setUnits('bytes')
class _Dot11RTSThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_Dot11RTSThresh_Type.__name__=_F
_Dot11RTSThresh_Object=MibScalar
dot11RTSThresh=_Dot11RTSThresh_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,7),_Dot11RTSThresh_Type())
dot11RTSThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RTSThresh.setStatus(_A)
class _Dot11SRL_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11SRL_Type.__name__=_F
_Dot11SRL_Object=MibScalar
dot11SRL=_Dot11SRL_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,8),_Dot11SRL_Type())
dot11SRL.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11SRL.setStatus(_A)
class _Dot11LRL_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11LRL_Type.__name__=_F
_Dot11LRL_Object=MibScalar
dot11LRL=_Dot11LRL_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,9),_Dot11LRL_Type())
dot11LRL.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11LRL.setStatus(_A)
class _Dot1154gNetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5)));namedValues=NamedValues(*(('mode54g11bOnly',0),('mode54gAuto',1),('mode54gPerformance',4),('mode54gLRS',5)))
_Dot1154gNetMode_Type.__name__=_C
_Dot1154gNetMode_Object=MibScalar
dot1154gNetMode=_Dot1154gNetMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,10),_Dot1154gNetMode_Type())
dot1154gNetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1154gNetMode.setStatus(_A)
class _Dot1154gProtectionEnable_Type(TruthValue):defaultValue=2
_Dot1154gProtectionEnable_Type.__name__=_P
_Dot1154gProtectionEnable_Object=MibScalar
dot1154gProtectionEnable=_Dot1154gProtectionEnable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,11),_Dot1154gProtectionEnable_Type())
dot1154gProtectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1154gProtectionEnable.setStatus(_A)
class _Dot11Rate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5,6,9,11,12,18,24,36,48,54)));namedValues=NamedValues(*((_L,0),('mbits1',1),('mbits2',2),('mbits5-5',5),('mbits6',6),('mbits9',9),('mbits11',11),('mbits12',12),('mbits18',18),('mbits24',24),('mbits36',36),('mbits48',48),('mbits54',54)))
_Dot11Rate_Type.__name__=_C
_Dot11Rate_Object=MibScalar
dot11Rate=_Dot11Rate_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,12),_Dot11Rate_Type())
dot11Rate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11Rate.setStatus(_A)
class _Dot11OutputPower_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(25,50,75,100)));namedValues=NamedValues(*(('percent25',25),('percent50',50),('percent75',75),('percent100',100)))
_Dot11OutputPower_Type.__name__=_C
_Dot11OutputPower_Object=MibScalar
dot11OutputPower=_Dot11OutputPower_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,13),_Dot11OutputPower_Type())
dot11OutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11OutputPower.setStatus(_A)
class _Dot11MbssUserControl_Type(Integer32):defaultValue=100
_Dot11MbssUserControl_Type.__name__=_C
_Dot11MbssUserControl_Object=MibScalar
dot11MbssUserControl=_Dot11MbssUserControl_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,14),_Dot11MbssUserControl_Type())
dot11MbssUserControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11MbssUserControl.setStatus(_A)
class _Dot11BasicRateSet_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('all',2)))
_Dot11BasicRateSet_Type.__name__=_C
_Dot11BasicRateSet_Object=MibScalar
dot11BasicRateSet=_Dot11BasicRateSet_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,15),_Dot11BasicRateSet_Type())
dot11BasicRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BasicRateSet.setStatus(_A)
class _Dot11NMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_Dot11NMode_Type.__name__=_C
_Dot11NMode_Object=MibScalar
dot11NMode=_Dot11NMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,16),_Dot11NMode_Type())
dot11NMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NMode.setStatus(_A)
class _Dot11NPhyRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_L,0),('legacy',1),('mbits6-5or13-5',2),('mbits19-5or40-5',4),('mbits58-5or121-5',8),('mbits65or135',9),('mbits13or27',10),('mbits26or54',11),('mbits39or81',12),('mbits52or108',13),('mbits78or162',14),('mbits104or216',15),('mbits117or243',16),('mbits130or270',17)))
_Dot11NPhyRate_Type.__name__=_C
_Dot11NPhyRate_Object=MibScalar
dot11NPhyRate=_Dot11NPhyRate_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,17),_Dot11NPhyRate_Type())
dot11NPhyRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NPhyRate.setStatus(_A)
class _Dot11NBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('band-2-4G',1),('band-5G',2)))
_Dot11NBand_Type.__name__=_C
_Dot11NBand_Object=MibScalar
dot11NBand=_Dot11NBand_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,18),_Dot11NBand_Type())
dot11NBand.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NBand.setStatus(_A)
class _Dot11NBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('width-20MHz',1),('width-40MHz',2)))
_Dot11NBandWidth_Type.__name__=_C
_Dot11NBandWidth_Object=MibScalar
dot11NBandWidth=_Dot11NBandWidth_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,19),_Dot11NBandWidth_Type())
dot11NBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NBandWidth.setStatus(_A)
class _Dot11NSideBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upper',1),('lower',2)))
_Dot11NSideBand_Type.__name__=_C
_Dot11NSideBand_Object=MibScalar
dot11NSideBand=_Dot11NSideBand_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,20),_Dot11NSideBand_Type())
dot11NSideBand.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NSideBand.setStatus(_A)
class _Dot11NProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_Dot11NProtection_Type.__name__=_C
_Dot11NProtection_Object=MibScalar
dot11NProtection=_Dot11NProtection_Object((1,3,6,1,4,1,4413,2,2,2,1,5,1,21),_Dot11NProtection_Type())
dot11NProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NProtection.setStatus(_A)
_Dot11MgmtPrivacy_ObjectIdentity=ObjectIdentity
dot11MgmtPrivacy=_Dot11MgmtPrivacy_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,5,2))
class _Dot11EncryptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('wep64',1),(_S,2),('tkip',3),('aes',4),(_T,5)))
_Dot11EncryptionMode_Type.__name__=_C
_Dot11EncryptionMode_Object=MibScalar
dot11EncryptionMode=_Dot11EncryptionMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,1),_Dot11EncryptionMode_Type())
dot11EncryptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11EncryptionMode.setStatus(_D)
class _Dot11WepPassPhrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot11WepPassPhrase_Type.__name__=_M
_Dot11WepPassPhrase_Object=MibScalar
dot11WepPassPhrase=_Dot11WepPassPhrase_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,2),_Dot11WepPassPhrase_Type())
dot11WepPassPhrase.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11WepPassPhrase.setStatus(_D)
class _Dot11DefaultKey_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Dot11DefaultKey_Type.__name__=_F
_Dot11DefaultKey_Object=MibScalar
dot11DefaultKey=_Dot11DefaultKey_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,3),_Dot11DefaultKey_Type())
dot11DefaultKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DefaultKey.setStatus(_D)
_Dot1164BitKeyTable_Object=MibTable
dot1164BitKeyTable=_Dot1164BitKeyTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,4))
if mibBuilder.loadTexts:dot1164BitKeyTable.setStatus(_D)
_Dot1164BitKeyEntry_Object=MibTableRow
dot1164BitKeyEntry=_Dot1164BitKeyEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,4,1))
dot1164BitKeyEntry.setIndexNames((0,_I,_U))
if mibBuilder.loadTexts:dot1164BitKeyEntry.setStatus(_D)
class _Dot1164BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Dot1164BitKeyIndex_Type.__name__=_C
_Dot1164BitKeyIndex_Object=MibTableColumn
dot1164BitKeyIndex=_Dot1164BitKeyIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,4,1,1),_Dot1164BitKeyIndex_Type())
dot1164BitKeyIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dot1164BitKeyIndex.setStatus(_D)
class _Dot1164BitKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Dot1164BitKeyValue_Type.__name__=_E
_Dot1164BitKeyValue_Object=MibTableColumn
dot1164BitKeyValue=_Dot1164BitKeyValue_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,4,1,2),_Dot1164BitKeyValue_Type())
dot1164BitKeyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1164BitKeyValue.setStatus(_D)
_Dot11128BitKeyTable_Object=MibTable
dot11128BitKeyTable=_Dot11128BitKeyTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,5))
if mibBuilder.loadTexts:dot11128BitKeyTable.setStatus(_D)
_Dot11128BitKeyEntry_Object=MibTableRow
dot11128BitKeyEntry=_Dot11128BitKeyEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,5,1))
dot11128BitKeyEntry.setIndexNames((0,_I,_V))
if mibBuilder.loadTexts:dot11128BitKeyEntry.setStatus(_D)
class _Dot11128BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Dot11128BitKeyIndex_Type.__name__=_C
_Dot11128BitKeyIndex_Object=MibTableColumn
dot11128BitKeyIndex=_Dot11128BitKeyIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,5,1,1),_Dot11128BitKeyIndex_Type())
dot11128BitKeyIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dot11128BitKeyIndex.setStatus(_D)
class _Dot11128BitKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_Dot11128BitKeyValue_Type.__name__=_E
_Dot11128BitKeyValue_Object=MibTableColumn
dot11128BitKeyValue=_Dot11128BitKeyValue_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,5,1,2),_Dot11128BitKeyValue_Type())
dot11128BitKeyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11128BitKeyValue.setStatus(_D)
class _Dot11NetAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_W,0),('ieee802dot1X',1),('wpa',2),('wpa-psk',3)))
_Dot11NetAuthMode_Type.__name__=_C
_Dot11NetAuthMode_Object=MibScalar
dot11NetAuthMode=_Dot11NetAuthMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,6),_Dot11NetAuthMode_Type())
dot11NetAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NetAuthMode.setStatus(_D)
class _Dot11WpaPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_Dot11WpaPreSharedKey_Type.__name__=_E
_Dot11WpaPreSharedKey_Object=MibScalar
dot11WpaPreSharedKey=_Dot11WpaPreSharedKey_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,7),_Dot11WpaPreSharedKey_Type())
dot11WpaPreSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11WpaPreSharedKey.setStatus(_D)
_Dot11WpaGroupRekeyInterval_Type=Unsigned32
_Dot11WpaGroupRekeyInterval_Object=MibScalar
dot11WpaGroupRekeyInterval=_Dot11WpaGroupRekeyInterval_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,8),_Dot11WpaGroupRekeyInterval_Type())
dot11WpaGroupRekeyInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11WpaGroupRekeyInterval.setStatus(_D)
if mibBuilder.loadTexts:dot11WpaGroupRekeyInterval.setUnits(_O)
_Dot11RadiusIp_Type=IpAddress
_Dot11RadiusIp_Object=MibScalar
dot11RadiusIp=_Dot11RadiusIp_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,9),_Dot11RadiusIp_Type())
dot11RadiusIp.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RadiusIp.setStatus(_D)
_Dot11RadiusPort_Type=Unsigned32
_Dot11RadiusPort_Object=MibScalar
dot11RadiusPort=_Dot11RadiusPort_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,10),_Dot11RadiusPort_Type())
dot11RadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RadiusPort.setStatus(_D)
_Dot11RadiusKey_Type=DisplayString
_Dot11RadiusKey_Object=MibScalar
dot11RadiusKey=_Dot11RadiusKey_Object((1,3,6,1,4,1,4413,2,2,2,1,5,2,11),_Dot11RadiusKey_Type())
dot11RadiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RadiusKey.setStatus(_D)
_Dot11MgmtAccess_ObjectIdentity=ObjectIdentity
dot11MgmtAccess=_Dot11MgmtAccess_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,5,3))
class _Dot11AuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sharedKeyOnly',1),('openSystemOrSharedKey',2)))
_Dot11AuthenticationMode_Type.__name__=_C
_Dot11AuthenticationMode_Object=MibScalar
dot11AuthenticationMode=_Dot11AuthenticationMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,3,1),_Dot11AuthenticationMode_Type())
dot11AuthenticationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationMode.setStatus(_D)
_Dot11ClosedNetwork_Type=TruthValue
_Dot11ClosedNetwork_Object=MibScalar
dot11ClosedNetwork=_Dot11ClosedNetwork_Object((1,3,6,1,4,1,4413,2,2,2,1,5,3,2),_Dot11ClosedNetwork_Type())
dot11ClosedNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ClosedNetwork.setStatus(_D)
class _Dot11AccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_X,0),(_Y,1),(_Z,2)))
_Dot11AccessMode_Type.__name__=_C
_Dot11AccessMode_Object=MibScalar
dot11AccessMode=_Dot11AccessMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,3,3),_Dot11AccessMode_Type())
dot11AccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AccessMode.setStatus(_D)
_Dot11AccessTable_Object=MibTable
dot11AccessTable=_Dot11AccessTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,3,5))
if mibBuilder.loadTexts:dot11AccessTable.setStatus(_D)
_Dot11AccessEntry_Object=MibTableRow
dot11AccessEntry=_Dot11AccessEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,3,5,1))
dot11AccessEntry.setIndexNames((0,_I,_a))
if mibBuilder.loadTexts:dot11AccessEntry.setStatus(_D)
class _Dot11AccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Dot11AccessIndex_Type.__name__=_C
_Dot11AccessIndex_Object=MibTableColumn
dot11AccessIndex=_Dot11AccessIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,5,3,5,1,1),_Dot11AccessIndex_Type())
dot11AccessIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dot11AccessIndex.setStatus(_D)
_Dot11AccessStation_Type=MacAddress
_Dot11AccessStation_Object=MibTableColumn
dot11AccessStation=_Dot11AccessStation_Object((1,3,6,1,4,1,4413,2,2,2,1,5,3,5,1,2),_Dot11AccessStation_Type())
dot11AccessStation.setMaxAccess(_J)
if mibBuilder.loadTexts:dot11AccessStation.setStatus(_D)
_Dot11MgmtMbss_ObjectIdentity=ObjectIdentity
dot11MgmtMbss=_Dot11MgmtMbss_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,5,4))
_Dot11MbssBase_ObjectIdentity=ObjectIdentity
dot11MbssBase=_Dot11MbssBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,5,4,1))
_Dot11BssTable_Object=MibTable
dot11BssTable=_Dot11BssTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14))
if mibBuilder.loadTexts:dot11BssTable.setStatus(_A)
_Dot11BssEntry_Object=MibTableRow
dot11BssEntry=_Dot11BssEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1))
dot11BssEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dot11BssEntry.setStatus(_A)
_Dot11BssId_Type=PhysAddress
_Dot11BssId_Object=MibTableColumn
dot11BssId=_Dot11BssId_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1,1),_Dot11BssId_Type())
dot11BssId.setMaxAccess('read-only')
if mibBuilder.loadTexts:dot11BssId.setStatus(_A)
_Dot11BssEnable_Type=TruthValue
_Dot11BssEnable_Object=MibTableColumn
dot11BssEnable=_Dot11BssEnable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1,2),_Dot11BssEnable_Type())
dot11BssEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssEnable.setStatus(_A)
class _Dot11BssSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot11BssSsid_Type.__name__=_E
_Dot11BssSsid_Object=MibTableColumn
dot11BssSsid=_Dot11BssSsid_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1,3),_Dot11BssSsid_Type())
dot11BssSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssSsid.setStatus(_A)
class _Dot11BssNetworkBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lan',1),('guest',2)))
_Dot11BssNetworkBridge_Type.__name__=_C
_Dot11BssNetworkBridge_Object=MibTableColumn
dot11BssNetworkBridge=_Dot11BssNetworkBridge_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1,4),_Dot11BssNetworkBridge_Type())
dot11BssNetworkBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssNetworkBridge.setStatus(_D)
class _Dot11BssSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_W,0),('wep',1),('wpaPsk',2),('wpa2Psk',3),('wpaEnterprise',4),('wpa2Enterprise',5),('radiusWep',6)))
_Dot11BssSecurityMode_Type.__name__=_C
_Dot11BssSecurityMode_Object=MibTableColumn
dot11BssSecurityMode=_Dot11BssSecurityMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1,5),_Dot11BssSecurityMode_Type())
dot11BssSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssSecurityMode.setStatus(_A)
_Dot11BssClosedNetwork_Type=TruthValue
_Dot11BssClosedNetwork_Object=MibTableColumn
dot11BssClosedNetwork=_Dot11BssClosedNetwork_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1,6),_Dot11BssClosedNetwork_Type())
dot11BssClosedNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssClosedNetwork.setStatus(_A)
class _Dot11BssAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3)))
_Dot11BssAccessMode_Type.__name__=_C
_Dot11BssAccessMode_Object=MibTableColumn
dot11BssAccessMode=_Dot11BssAccessMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,1,14,1,7),_Dot11BssAccessMode_Type())
dot11BssAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssAccessMode.setStatus(_A)
_Dot11MbssSecurity_ObjectIdentity=ObjectIdentity
dot11MbssSecurity=_Dot11MbssSecurity_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,5,4,2))
_Dot11BssWepTable_Object=MibTable
dot11BssWepTable=_Dot11BssWepTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,1))
if mibBuilder.loadTexts:dot11BssWepTable.setStatus(_A)
_Dot11BssWepEntry_Object=MibTableRow
dot11BssWepEntry=_Dot11BssWepEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,1,1))
dot11BssWepEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dot11BssWepEntry.setStatus(_A)
_Dot11BssWepDefaultKey_Type=Unsigned32
_Dot11BssWepDefaultKey_Object=MibTableColumn
dot11BssWepDefaultKey=_Dot11BssWepDefaultKey_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,1,1,1),_Dot11BssWepDefaultKey_Type())
dot11BssWepDefaultKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssWepDefaultKey.setStatus(_A)
class _Dot11BssWepEncryptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wep64',1),(_S,2)))
_Dot11BssWepEncryptionMode_Type.__name__=_C
_Dot11BssWepEncryptionMode_Object=MibTableColumn
dot11BssWepEncryptionMode=_Dot11BssWepEncryptionMode_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,1,1,2),_Dot11BssWepEncryptionMode_Type())
dot11BssWepEncryptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssWepEncryptionMode.setStatus(_A)
class _Dot11BssWepPassPhrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot11BssWepPassPhrase_Type.__name__=_M
_Dot11BssWepPassPhrase_Object=MibTableColumn
dot11BssWepPassPhrase=_Dot11BssWepPassPhrase_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,1,1,3),_Dot11BssWepPassPhrase_Type())
dot11BssWepPassPhrase.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssWepPassPhrase.setStatus(_A)
_Dot11BssWep64BitKeyTable_Object=MibTable
dot11BssWep64BitKeyTable=_Dot11BssWep64BitKeyTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,2))
if mibBuilder.loadTexts:dot11BssWep64BitKeyTable.setStatus(_A)
_Dot11BssWep64BitKeyEntry_Object=MibTableRow
dot11BssWep64BitKeyEntry=_Dot11BssWep64BitKeyEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,2,1))
dot11BssWep64BitKeyEntry.setIndexNames((0,_G,_H),(0,_I,_b))
if mibBuilder.loadTexts:dot11BssWep64BitKeyEntry.setStatus(_A)
class _Dot11BssWep64BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Dot11BssWep64BitKeyIndex_Type.__name__=_C
_Dot11BssWep64BitKeyIndex_Object=MibTableColumn
dot11BssWep64BitKeyIndex=_Dot11BssWep64BitKeyIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,2,1,1),_Dot11BssWep64BitKeyIndex_Type())
dot11BssWep64BitKeyIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dot11BssWep64BitKeyIndex.setStatus(_A)
class _Dot11BssWep64BitKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Dot11BssWep64BitKeyValue_Type.__name__=_E
_Dot11BssWep64BitKeyValue_Object=MibTableColumn
dot11BssWep64BitKeyValue=_Dot11BssWep64BitKeyValue_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,2,1,2),_Dot11BssWep64BitKeyValue_Type())
dot11BssWep64BitKeyValue.setMaxAccess(_J)
if mibBuilder.loadTexts:dot11BssWep64BitKeyValue.setStatus(_A)
_Dot11BssWep64BitKeyStatus_Type=RowStatus
_Dot11BssWep64BitKeyStatus_Object=MibTableColumn
dot11BssWep64BitKeyStatus=_Dot11BssWep64BitKeyStatus_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,2,1,3),_Dot11BssWep64BitKeyStatus_Type())
dot11BssWep64BitKeyStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:dot11BssWep64BitKeyStatus.setStatus(_A)
_Dot11BssWep128BitKeyTable_Object=MibTable
dot11BssWep128BitKeyTable=_Dot11BssWep128BitKeyTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,3))
if mibBuilder.loadTexts:dot11BssWep128BitKeyTable.setStatus(_A)
_Dot11BssWep128BitKeyEntry_Object=MibTableRow
dot11BssWep128BitKeyEntry=_Dot11BssWep128BitKeyEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,3,1))
dot11BssWep128BitKeyEntry.setIndexNames((0,_G,_H),(0,_I,_c))
if mibBuilder.loadTexts:dot11BssWep128BitKeyEntry.setStatus(_A)
class _Dot11BssWep128BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Dot11BssWep128BitKeyIndex_Type.__name__=_C
_Dot11BssWep128BitKeyIndex_Object=MibTableColumn
dot11BssWep128BitKeyIndex=_Dot11BssWep128BitKeyIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,3,1,1),_Dot11BssWep128BitKeyIndex_Type())
dot11BssWep128BitKeyIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dot11BssWep128BitKeyIndex.setStatus(_A)
class _Dot11BssWep128BitKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_Dot11BssWep128BitKeyValue_Type.__name__=_E
_Dot11BssWep128BitKeyValue_Object=MibTableColumn
dot11BssWep128BitKeyValue=_Dot11BssWep128BitKeyValue_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,3,1,2),_Dot11BssWep128BitKeyValue_Type())
dot11BssWep128BitKeyValue.setMaxAccess(_J)
if mibBuilder.loadTexts:dot11BssWep128BitKeyValue.setStatus(_A)
_Dot11BssWep128BitKeyStatus_Type=RowStatus
_Dot11BssWep128BitKeyStatus_Object=MibTableColumn
dot11BssWep128BitKeyStatus=_Dot11BssWep128BitKeyStatus_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,3,1,3),_Dot11BssWep128BitKeyStatus_Type())
dot11BssWep128BitKeyStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:dot11BssWep128BitKeyStatus.setStatus(_A)
_Dot11BssWpaTable_Object=MibTable
dot11BssWpaTable=_Dot11BssWpaTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,4))
if mibBuilder.loadTexts:dot11BssWpaTable.setStatus(_A)
_Dot11BssWpaEntry_Object=MibTableRow
dot11BssWpaEntry=_Dot11BssWpaEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,4,1))
dot11BssWpaEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dot11BssWpaEntry.setStatus(_A)
class _Dot11BssWpaAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tkip',1),('aes',2),(_T,3)))
_Dot11BssWpaAlgorithm_Type.__name__=_C
_Dot11BssWpaAlgorithm_Object=MibTableColumn
dot11BssWpaAlgorithm=_Dot11BssWpaAlgorithm_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,4,1,1),_Dot11BssWpaAlgorithm_Type())
dot11BssWpaAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssWpaAlgorithm.setStatus(_A)
class _Dot11BssWpaPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_Dot11BssWpaPreSharedKey_Type.__name__=_E
_Dot11BssWpaPreSharedKey_Object=MibTableColumn
dot11BssWpaPreSharedKey=_Dot11BssWpaPreSharedKey_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,4,1,2),_Dot11BssWpaPreSharedKey_Type())
dot11BssWpaPreSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssWpaPreSharedKey.setStatus(_A)
_Dot11BssWpaGroupRekeyInterval_Type=Unsigned32
_Dot11BssWpaGroupRekeyInterval_Object=MibTableColumn
dot11BssWpaGroupRekeyInterval=_Dot11BssWpaGroupRekeyInterval_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,4,1,3),_Dot11BssWpaGroupRekeyInterval_Type())
dot11BssWpaGroupRekeyInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssWpaGroupRekeyInterval.setStatus(_A)
if mibBuilder.loadTexts:dot11BssWpaGroupRekeyInterval.setUnits(_O)
_Dot11BssRadiusTable_Object=MibTable
dot11BssRadiusTable=_Dot11BssRadiusTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,5))
if mibBuilder.loadTexts:dot11BssRadiusTable.setStatus(_A)
_Dot11BssRadiusEntry_Object=MibTableRow
dot11BssRadiusEntry=_Dot11BssRadiusEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,5,1))
dot11BssRadiusEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dot11BssRadiusEntry.setStatus(_A)
_Dot11BssRadiusAddressType_Type=InetAddressType
_Dot11BssRadiusAddressType_Object=MibTableColumn
dot11BssRadiusAddressType=_Dot11BssRadiusAddressType_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,5,1,1),_Dot11BssRadiusAddressType_Type())
dot11BssRadiusAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssRadiusAddressType.setStatus(_A)
_Dot11BssRadiusAddress_Type=InetAddress
_Dot11BssRadiusAddress_Object=MibTableColumn
dot11BssRadiusAddress=_Dot11BssRadiusAddress_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,5,1,2),_Dot11BssRadiusAddress_Type())
dot11BssRadiusAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssRadiusAddress.setStatus(_A)
_Dot11BssRadiusPort_Type=Unsigned32
_Dot11BssRadiusPort_Object=MibTableColumn
dot11BssRadiusPort=_Dot11BssRadiusPort_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,5,1,3),_Dot11BssRadiusPort_Type())
dot11BssRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssRadiusPort.setStatus(_A)
_Dot11BssRadiusKey_Type=DisplayString
_Dot11BssRadiusKey_Object=MibTableColumn
dot11BssRadiusKey=_Dot11BssRadiusKey_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,5,1,4),_Dot11BssRadiusKey_Type())
dot11BssRadiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssRadiusKey.setStatus(_A)
_Dot11BssRadiusReAuthInterval_Type=Unsigned32
_Dot11BssRadiusReAuthInterval_Object=MibTableColumn
dot11BssRadiusReAuthInterval=_Dot11BssRadiusReAuthInterval_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,2,5,1,5),_Dot11BssRadiusReAuthInterval_Type())
dot11BssRadiusReAuthInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11BssRadiusReAuthInterval.setStatus(_A)
if mibBuilder.loadTexts:dot11BssRadiusReAuthInterval.setUnits(_O)
_Dot11MbssAccess_ObjectIdentity=ObjectIdentity
dot11MbssAccess=_Dot11MbssAccess_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,5,4,3))
_Dot11BssAccessTable_Object=MibTable
dot11BssAccessTable=_Dot11BssAccessTable_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,3,1))
if mibBuilder.loadTexts:dot11BssAccessTable.setStatus(_A)
_Dot11BssAccessEntry_Object=MibTableRow
dot11BssAccessEntry=_Dot11BssAccessEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,3,1,1))
dot11BssAccessEntry.setIndexNames((0,_G,_H),(0,_I,_d))
if mibBuilder.loadTexts:dot11BssAccessEntry.setStatus(_A)
class _Dot11BssAccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Dot11BssAccessIndex_Type.__name__=_C
_Dot11BssAccessIndex_Object=MibTableColumn
dot11BssAccessIndex=_Dot11BssAccessIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,3,1,1,1),_Dot11BssAccessIndex_Type())
dot11BssAccessIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dot11BssAccessIndex.setStatus(_A)
_Dot11BssAccessStation_Type=PhysAddress
_Dot11BssAccessStation_Object=MibTableColumn
dot11BssAccessStation=_Dot11BssAccessStation_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,3,1,1,2),_Dot11BssAccessStation_Type())
dot11BssAccessStation.setMaxAccess(_J)
if mibBuilder.loadTexts:dot11BssAccessStation.setStatus(_A)
_Dot11BssAccessStatus_Type=RowStatus
_Dot11BssAccessStatus_Object=MibTableColumn
dot11BssAccessStatus=_Dot11BssAccessStatus_Object((1,3,6,1,4,1,4413,2,2,2,1,5,4,3,1,1,3),_Dot11BssAccessStatus_Type())
dot11BssAccessStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:dot11BssAccessStatus.setStatus(_A)
_Dot11ApplySettings_Type=TruthValue
_Dot11ApplySettings_Object=MibScalar
dot11ApplySettings=_Dot11ApplySettings_Object((1,3,6,1,4,1,4413,2,2,2,1,5,100),_Dot11ApplySettings_Type())
dot11ApplySettings.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ApplySettings.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'ieee802dot11Mgmt':ieee802dot11Mgmt,'dot11MgmtBase':dot11MgmtBase,'dot11OperMode':dot11OperMode,'dot11SSID':dot11SSID,'dot11CurrentChannel':dot11CurrentChannel,'dot11BeaconInterval':dot11BeaconInterval,'dot11DTIMInterval':dot11DTIMInterval,'dot11FragThresh':dot11FragThresh,'dot11RTSThresh':dot11RTSThresh,'dot11SRL':dot11SRL,'dot11LRL':dot11LRL,'dot1154gNetMode':dot1154gNetMode,'dot1154gProtectionEnable':dot1154gProtectionEnable,'dot11Rate':dot11Rate,'dot11OutputPower':dot11OutputPower,'dot11MbssUserControl':dot11MbssUserControl,'dot11BasicRateSet':dot11BasicRateSet,'dot11NMode':dot11NMode,'dot11NPhyRate':dot11NPhyRate,'dot11NBand':dot11NBand,'dot11NBandWidth':dot11NBandWidth,'dot11NSideBand':dot11NSideBand,'dot11NProtection':dot11NProtection,'dot11MgmtPrivacy':dot11MgmtPrivacy,'dot11EncryptionMode':dot11EncryptionMode,'dot11WepPassPhrase':dot11WepPassPhrase,'dot11DefaultKey':dot11DefaultKey,'dot1164BitKeyTable':dot1164BitKeyTable,'dot1164BitKeyEntry':dot1164BitKeyEntry,_U:dot1164BitKeyIndex,'dot1164BitKeyValue':dot1164BitKeyValue,'dot11128BitKeyTable':dot11128BitKeyTable,'dot11128BitKeyEntry':dot11128BitKeyEntry,_V:dot11128BitKeyIndex,'dot11128BitKeyValue':dot11128BitKeyValue,'dot11NetAuthMode':dot11NetAuthMode,'dot11WpaPreSharedKey':dot11WpaPreSharedKey,'dot11WpaGroupRekeyInterval':dot11WpaGroupRekeyInterval,'dot11RadiusIp':dot11RadiusIp,'dot11RadiusPort':dot11RadiusPort,'dot11RadiusKey':dot11RadiusKey,'dot11MgmtAccess':dot11MgmtAccess,'dot11AuthenticationMode':dot11AuthenticationMode,'dot11ClosedNetwork':dot11ClosedNetwork,'dot11AccessMode':dot11AccessMode,'dot11AccessTable':dot11AccessTable,'dot11AccessEntry':dot11AccessEntry,_a:dot11AccessIndex,'dot11AccessStation':dot11AccessStation,'dot11MgmtMbss':dot11MgmtMbss,'dot11MbssBase':dot11MbssBase,'dot11BssTable':dot11BssTable,'dot11BssEntry':dot11BssEntry,'dot11BssId':dot11BssId,'dot11BssEnable':dot11BssEnable,'dot11BssSsid':dot11BssSsid,'dot11BssNetworkBridge':dot11BssNetworkBridge,'dot11BssSecurityMode':dot11BssSecurityMode,'dot11BssClosedNetwork':dot11BssClosedNetwork,'dot11BssAccessMode':dot11BssAccessMode,'dot11MbssSecurity':dot11MbssSecurity,'dot11BssWepTable':dot11BssWepTable,'dot11BssWepEntry':dot11BssWepEntry,'dot11BssWepDefaultKey':dot11BssWepDefaultKey,'dot11BssWepEncryptionMode':dot11BssWepEncryptionMode,'dot11BssWepPassPhrase':dot11BssWepPassPhrase,'dot11BssWep64BitKeyTable':dot11BssWep64BitKeyTable,'dot11BssWep64BitKeyEntry':dot11BssWep64BitKeyEntry,_b:dot11BssWep64BitKeyIndex,'dot11BssWep64BitKeyValue':dot11BssWep64BitKeyValue,'dot11BssWep64BitKeyStatus':dot11BssWep64BitKeyStatus,'dot11BssWep128BitKeyTable':dot11BssWep128BitKeyTable,'dot11BssWep128BitKeyEntry':dot11BssWep128BitKeyEntry,_c:dot11BssWep128BitKeyIndex,'dot11BssWep128BitKeyValue':dot11BssWep128BitKeyValue,'dot11BssWep128BitKeyStatus':dot11BssWep128BitKeyStatus,'dot11BssWpaTable':dot11BssWpaTable,'dot11BssWpaEntry':dot11BssWpaEntry,'dot11BssWpaAlgorithm':dot11BssWpaAlgorithm,'dot11BssWpaPreSharedKey':dot11BssWpaPreSharedKey,'dot11BssWpaGroupRekeyInterval':dot11BssWpaGroupRekeyInterval,'dot11BssRadiusTable':dot11BssRadiusTable,'dot11BssRadiusEntry':dot11BssRadiusEntry,'dot11BssRadiusAddressType':dot11BssRadiusAddressType,'dot11BssRadiusAddress':dot11BssRadiusAddress,'dot11BssRadiusPort':dot11BssRadiusPort,'dot11BssRadiusKey':dot11BssRadiusKey,'dot11BssRadiusReAuthInterval':dot11BssRadiusReAuthInterval,'dot11MbssAccess':dot11MbssAccess,'dot11BssAccessTable':dot11BssAccessTable,'dot11BssAccessEntry':dot11BssAccessEntry,_d:dot11BssAccessIndex,'dot11BssAccessStation':dot11BssAccessStation,'dot11BssAccessStatus':dot11BssAccessStatus,'dot11ApplySettings':dot11ApplySettings})