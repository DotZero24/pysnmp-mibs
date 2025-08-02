_N='swConnUnitPortEntry'
_M='swPortConfigEntry'
_L='swPortFapwwnConfigEntry'
_K='swSfpStatEntry'
_J='notsupported'
_I='disabled'
_H='enabled'
_G='DisplayString'
_F='unknown'
_E='FA-EXT-MIB'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
connUnitPortEntry,=mibBuilder.importSymbols('FCMGMT-MIB','connUnitPortEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
sw,=mibBuilder.importSymbols('SW-MIB','sw')
faExt=ModuleIdentity((1,3,6,1,4,1,1588,2,1,1,1,28))
if mibBuilder.loadTexts:faExt.setRevisions(('2010-11-22 10:30','2013-09-12 10:30','2013-09-24 13:55','2013-10-29 13:54'))
class FapwwnType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('auto',2),('userConfigured',3)))
class CiperMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('allFrames',2),('fcpAndNonFCP',3),('onlyFCP',4)))
class EncryptCompressStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SwSfpStatTable_Object=MibTable
swSfpStatTable=_SwSfpStatTable_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1))
if mibBuilder.loadTexts:swSfpStatTable.setStatus(_A)
_SwSfpStatEntry_Object=MibTableRow
swSfpStatEntry=_SwSfpStatEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1))
if mibBuilder.loadTexts:swSfpStatEntry.setStatus(_A)
class _SwSfpTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwSfpTemperature_Type.__name__=_C
_SwSfpTemperature_Object=MibTableColumn
swSfpTemperature=_SwSfpTemperature_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1,1),_SwSfpTemperature_Type())
swSfpTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:swSfpTemperature.setStatus(_A)
if mibBuilder.loadTexts:swSfpTemperature.setUnits('centigrade')
class _SwSfpVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwSfpVoltage_Type.__name__=_C
_SwSfpVoltage_Object=MibTableColumn
swSfpVoltage=_SwSfpVoltage_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1,2),_SwSfpVoltage_Type())
swSfpVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:swSfpVoltage.setStatus(_A)
if mibBuilder.loadTexts:swSfpVoltage.setUnits('milli voltage')
class _SwSfpCurrent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwSfpCurrent_Type.__name__=_C
_SwSfpCurrent_Object=MibTableColumn
swSfpCurrent=_SwSfpCurrent_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1,3),_SwSfpCurrent_Type())
swSfpCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:swSfpCurrent.setStatus(_A)
if mibBuilder.loadTexts:swSfpCurrent.setUnits('milli amphere')
class _SwSfpRxPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwSfpRxPower_Type.__name__=_C
_SwSfpRxPower_Object=MibTableColumn
swSfpRxPower=_SwSfpRxPower_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1,4),_SwSfpRxPower_Type())
swSfpRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:swSfpRxPower.setStatus(_A)
if mibBuilder.loadTexts:swSfpRxPower.setUnits('dBm')
class _SwSfpTxPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwSfpTxPower_Type.__name__=_C
_SwSfpTxPower_Object=MibTableColumn
swSfpTxPower=_SwSfpTxPower_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1,5),_SwSfpTxPower_Type())
swSfpTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:swSfpTxPower.setStatus(_A)
if mibBuilder.loadTexts:swSfpTxPower.setUnits('dBm')
_SwSfpPoweronHrs_Type=Integer32
_SwSfpPoweronHrs_Object=MibTableColumn
swSfpPoweronHrs=_SwSfpPoweronHrs_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1,6),_SwSfpPoweronHrs_Type())
swSfpPoweronHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:swSfpPoweronHrs.setStatus(_A)
if mibBuilder.loadTexts:swSfpPoweronHrs.setUnits('hours')
_SwSfpUnitId_Type=Integer32
_SwSfpUnitId_Object=MibTableColumn
swSfpUnitId=_SwSfpUnitId_Object((1,3,6,1,4,1,1588,2,1,1,1,28,1,1,7),_SwSfpUnitId_Type())
swSfpUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:swSfpUnitId.setStatus(_A)
_SwFapwwnFeature_ObjectIdentity=ObjectIdentity
swFapwwnFeature=_SwFapwwnFeature_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,28,2))
if mibBuilder.loadTexts:swFapwwnFeature.setStatus(_A)
_SwPortFapwwnConfigTable_Object=MibTable
swPortFapwwnConfigTable=_SwPortFapwwnConfigTable_Object((1,3,6,1,4,1,1588,2,1,1,1,28,2,1))
if mibBuilder.loadTexts:swPortFapwwnConfigTable.setStatus(_A)
_SwPortFapwwnConfigEntry_Object=MibTableRow
swPortFapwwnConfigEntry=_SwPortFapwwnConfigEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,28,2,1,1))
if mibBuilder.loadTexts:swPortFapwwnConfigEntry.setStatus(_A)
_SwPortFapwwnConfigEnable_Type=TruthValue
_SwPortFapwwnConfigEnable_Object=MibTableColumn
swPortFapwwnConfigEnable=_SwPortFapwwnConfigEnable_Object((1,3,6,1,4,1,1588,2,1,1,1,28,2,1,1,1),_SwPortFapwwnConfigEnable_Type())
swPortFapwwnConfigEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFapwwnConfigEnable.setStatus(_A)
class _SwPortFapwwnConfigFapwwn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_SwPortFapwwnConfigFapwwn_Type.__name__=_G
_SwPortFapwwnConfigFapwwn_Object=MibTableColumn
swPortFapwwnConfigFapwwn=_SwPortFapwwnConfigFapwwn_Object((1,3,6,1,4,1,1588,2,1,1,1,28,2,1,1,2),_SwPortFapwwnConfigFapwwn_Type())
swPortFapwwnConfigFapwwn.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFapwwnConfigFapwwn.setStatus(_A)
_SwPortFapwwnConfigType_Type=FapwwnType
_SwPortFapwwnConfigType_Object=MibTableColumn
swPortFapwwnConfigType=_SwPortFapwwnConfigType_Object((1,3,6,1,4,1,1588,2,1,1,1,28,2,1,1,3),_SwPortFapwwnConfigType_Type())
swPortFapwwnConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortFapwwnConfigType.setStatus(_A)
_SwPortConfigTable_Object=MibTable
swPortConfigTable=_SwPortConfigTable_Object((1,3,6,1,4,1,1588,2,1,1,1,28,3))
if mibBuilder.loadTexts:swPortConfigTable.setStatus(_A)
_SwPortConfigEntry_Object=MibTableRow
swPortConfigEntry=_SwPortConfigEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,28,3,1))
if mibBuilder.loadTexts:swPortConfigEntry.setStatus(_A)
_SwPortEncrypt_Type=EncryptCompressStatus
_SwPortEncrypt_Object=MibTableColumn
swPortEncrypt=_SwPortEncrypt_Object((1,3,6,1,4,1,1588,2,1,1,1,28,3,1,1),_SwPortEncrypt_Type())
swPortEncrypt.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortEncrypt.setStatus(_A)
_SwPortCompression_Type=EncryptCompressStatus
_SwPortCompression_Object=MibTableColumn
swPortCompression=_SwPortCompression_Object((1,3,6,1,4,1,1588,2,1,1,1,28,3,1,2),_SwPortCompression_Type())
swPortCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCompression.setStatus(_A)
class _SwPortCipherKeySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwPortCipherKeySize_Type.__name__=_D
_SwPortCipherKeySize_Object=MibTableColumn
swPortCipherKeySize=_SwPortCipherKeySize_Object((1,3,6,1,4,1,1588,2,1,1,1,28,3,1,3),_SwPortCipherKeySize_Type())
swPortCipherKeySize.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCipherKeySize.setStatus(_A)
_SwPortCipherMode_Type=CiperMode
_SwPortCipherMode_Object=MibTableColumn
swPortCipherMode=_SwPortCipherMode_Object((1,3,6,1,4,1,1588,2,1,1,1,28,3,1,4),_SwPortCipherMode_Type())
swPortCipherMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortCipherMode.setStatus(_A)
_SwConnUnitPortTable_Object=MibTable
swConnUnitPortTable=_SwConnUnitPortTable_Object((1,3,6,1,4,1,1588,2,1,1,1,28,4))
if mibBuilder.loadTexts:swConnUnitPortTable.setStatus(_A)
_SwConnUnitPortEntry_Object=MibTableRow
swConnUnitPortEntry=_SwConnUnitPortEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,28,4,1))
if mibBuilder.loadTexts:swConnUnitPortEntry.setStatus(_A)
_SwConnUnitPortCapableSpeeds_Type=OctetString
_SwConnUnitPortCapableSpeeds_Object=MibTableColumn
swConnUnitPortCapableSpeeds=_SwConnUnitPortCapableSpeeds_Object((1,3,6,1,4,1,1588,2,1,1,1,28,4,1,1),_SwConnUnitPortCapableSpeeds_Type())
swConnUnitPortCapableSpeeds.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitPortCapableSpeeds.setStatus(_A)
class _SwConnUnitPortSpeedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto-neg',1),('static',2)))
_SwConnUnitPortSpeedMode_Type.__name__=_D
_SwConnUnitPortSpeedMode_Object=MibTableColumn
swConnUnitPortSpeedMode=_SwConnUnitPortSpeedMode_Object((1,3,6,1,4,1,1588,2,1,1,1,28,4,1,2),_SwConnUnitPortSpeedMode_Type())
swConnUnitPortSpeedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitPortSpeedMode.setStatus(_A)
class _SwConnUnitPortFECMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_H,3),(_J,4)))
_SwConnUnitPortFECMode_Type.__name__=_D
_SwConnUnitPortFECMode_Object=MibTableColumn
swConnUnitPortFECMode=_SwConnUnitPortFECMode_Object((1,3,6,1,4,1,1588,2,1,1,1,28,4,1,3),_SwConnUnitPortFECMode_Type())
swConnUnitPortFECMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitPortFECMode.setStatus(_A)
class _SwConnUnitPortFECState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('active',1),('inactive',2),(_J,3)))
_SwConnUnitPortFECState_Type.__name__=_D
_SwConnUnitPortFECState_Object=MibTableColumn
swConnUnitPortFECState=_SwConnUnitPortFECState_Object((1,3,6,1,4,1,1588,2,1,1,1,28,4,1,4),_SwConnUnitPortFECState_Type())
swConnUnitPortFECState.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitPortFECState.setStatus(_A)
connUnitPortEntry.registerAugmentions((_E,_K))
swSfpStatEntry.setIndexNames(*connUnitPortEntry.getIndexNames())
connUnitPortEntry.registerAugmentions((_E,_L))
swPortFapwwnConfigEntry.setIndexNames(*connUnitPortEntry.getIndexNames())
connUnitPortEntry.registerAugmentions((_E,_M))
swPortConfigEntry.setIndexNames(*connUnitPortEntry.getIndexNames())
connUnitPortEntry.registerAugmentions((_E,_N))
swConnUnitPortEntry.setIndexNames(*connUnitPortEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'FapwwnType':FapwwnType,'CiperMode':CiperMode,'EncryptCompressStatus':EncryptCompressStatus,'faExt':faExt,'swSfpStatTable':swSfpStatTable,_K:swSfpStatEntry,'swSfpTemperature':swSfpTemperature,'swSfpVoltage':swSfpVoltage,'swSfpCurrent':swSfpCurrent,'swSfpRxPower':swSfpRxPower,'swSfpTxPower':swSfpTxPower,'swSfpPoweronHrs':swSfpPoweronHrs,'swSfpUnitId':swSfpUnitId,'swFapwwnFeature':swFapwwnFeature,'swPortFapwwnConfigTable':swPortFapwwnConfigTable,_L:swPortFapwwnConfigEntry,'swPortFapwwnConfigEnable':swPortFapwwnConfigEnable,'swPortFapwwnConfigFapwwn':swPortFapwwnConfigFapwwn,'swPortFapwwnConfigType':swPortFapwwnConfigType,'swPortConfigTable':swPortConfigTable,_M:swPortConfigEntry,'swPortEncrypt':swPortEncrypt,'swPortCompression':swPortCompression,'swPortCipherKeySize':swPortCipherKeySize,'swPortCipherMode':swPortCipherMode,'swConnUnitPortTable':swConnUnitPortTable,_N:swConnUnitPortEntry,'swConnUnitPortCapableSpeeds':swConnUnitPortCapableSpeeds,'swConnUnitPortSpeedMode':swConnUnitPortSpeedMode,'swConnUnitPortFECMode':swConnUnitPortFECMode,'swConnUnitPortFECState':swConnUnitPortFECState})