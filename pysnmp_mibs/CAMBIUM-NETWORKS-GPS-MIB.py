_T='cnGpsSignalStatus'
_S='three-D'
_R='no-fix'
_Q='manual'
_P='automatic'
_O='rtk-float'
_N='rtk-fixed'
_M='diff-gps-fix'
_L='gps-fix'
_K='fix-not-valid'
_J='not-set'
_I='cnGpsPortIndex'
_H='CAMBIUM-NETWORKS-GPS-MIB'
_G='disabled'
_F='enabled'
_E='read-write'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnGpsMib=ModuleIdentity((1,3,6,1,4,1,17713,24,5))
if mibBuilder.loadTexts:cnGpsMib.setRevisions(('2020-06-29 00:00',))
_CnGpsObjects_ObjectIdentity=ObjectIdentity
cnGpsObjects=_CnGpsObjects_ObjectIdentity((1,3,6,1,4,1,17713,24,5,0))
class _CnGpsInternalSourceAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CnGpsInternalSourceAdminStatus_Type.__name__=_C
_CnGpsInternalSourceAdminStatus_Object=MibScalar
cnGpsInternalSourceAdminStatus=_CnGpsInternalSourceAdminStatus_Object((1,3,6,1,4,1,17713,24,5,0,1),_CnGpsInternalSourceAdminStatus_Type())
cnGpsInternalSourceAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnGpsInternalSourceAdminStatus.setStatus(_A)
class _CnGpsExternalSourceAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CnGpsExternalSourceAdminStatus_Type.__name__=_C
_CnGpsExternalSourceAdminStatus_Object=MibScalar
cnGpsExternalSourceAdminStatus=_CnGpsExternalSourceAdminStatus_Object((1,3,6,1,4,1,17713,24,5,0,2),_CnGpsExternalSourceAdminStatus_Type())
cnGpsExternalSourceAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnGpsExternalSourceAdminStatus.setStatus(_A)
_CnGpsPortTable_Object=MibTable
cnGpsPortTable=_CnGpsPortTable_Object((1,3,6,1,4,1,17713,24,5,0,3))
if mibBuilder.loadTexts:cnGpsPortTable.setStatus(_A)
_CnGpsPortEntry_Object=MibTableRow
cnGpsPortEntry=_CnGpsPortEntry_Object((1,3,6,1,4,1,17713,24,5,0,3,1))
cnGpsPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cnGpsPortEntry.setStatus(_A)
class _CnGpsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnGpsPortIndex_Type.__name__=_C
_CnGpsPortIndex_Object=MibTableColumn
cnGpsPortIndex=_CnGpsPortIndex_Object((1,3,6,1,4,1,17713,24,5,0,3,1,1),_CnGpsPortIndex_Type())
cnGpsPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnGpsPortIndex.setStatus(_A)
class _CnGpsPortOutputAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CnGpsPortOutputAdminStatus_Type.__name__=_C
_CnGpsPortOutputAdminStatus_Object=MibTableColumn
cnGpsPortOutputAdminStatus=_CnGpsPortOutputAdminStatus_Object((1,3,6,1,4,1,17713,24,5,0,3,1,2),_CnGpsPortOutputAdminStatus_Type())
cnGpsPortOutputAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnGpsPortOutputAdminStatus.setStatus(_A)
class _CnGpsSignalStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('not-enabled-sources',1),('not-acquired',2),('acquired',3)))
_CnGpsSignalStatus_Type.__name__=_C
_CnGpsSignalStatus_Object=MibScalar
cnGpsSignalStatus=_CnGpsSignalStatus_Object((1,3,6,1,4,1,17713,24,5,0,4),_CnGpsSignalStatus_Type())
cnGpsSignalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsSignalStatus.setStatus(_A)
class _CnGpsSourcePowerCycle_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('internal',1),('external',2)))
_CnGpsSourcePowerCycle_Type.__name__=_C
_CnGpsSourcePowerCycle_Object=MibScalar
cnGpsSourcePowerCycle=_CnGpsSourcePowerCycle_Object((1,3,6,1,4,1,17713,24,5,0,6),_CnGpsSourcePowerCycle_Type())
cnGpsSourcePowerCycle.setMaxAccess(_E)
if mibBuilder.loadTexts:cnGpsSourcePowerCycle.setStatus(_A)
class _CnGpsInternalTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalTime_Type.__name__=_D
_CnGpsInternalTime_Object=MibScalar
cnGpsInternalTime=_CnGpsInternalTime_Object((1,3,6,1,4,1,17713,24,5,0,7),_CnGpsInternalTime_Type())
cnGpsInternalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalTime.setStatus(_A)
class _CnGpsExternalTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalTime_Type.__name__=_D
_CnGpsExternalTime_Object=MibScalar
cnGpsExternalTime=_CnGpsExternalTime_Object((1,3,6,1,4,1,17713,24,5,0,8),_CnGpsExternalTime_Type())
cnGpsExternalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalTime.setStatus(_A)
class _CnGpsInternalLatitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalLatitude_Type.__name__=_D
_CnGpsInternalLatitude_Object=MibScalar
cnGpsInternalLatitude=_CnGpsInternalLatitude_Object((1,3,6,1,4,1,17713,24,5,0,9),_CnGpsInternalLatitude_Type())
cnGpsInternalLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalLatitude.setStatus(_A)
class _CnGpsExternalLatitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalLatitude_Type.__name__=_D
_CnGpsExternalLatitude_Object=MibScalar
cnGpsExternalLatitude=_CnGpsExternalLatitude_Object((1,3,6,1,4,1,17713,24,5,0,10),_CnGpsExternalLatitude_Type())
cnGpsExternalLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalLatitude.setStatus(_A)
class _CnGpsInternalLongitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalLongitude_Type.__name__=_D
_CnGpsInternalLongitude_Object=MibScalar
cnGpsInternalLongitude=_CnGpsInternalLongitude_Object((1,3,6,1,4,1,17713,24,5,0,11),_CnGpsInternalLongitude_Type())
cnGpsInternalLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalLongitude.setStatus(_A)
class _CnGpsExternalLongitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalLongitude_Type.__name__=_D
_CnGpsExternalLongitude_Object=MibScalar
cnGpsExternalLongitude=_CnGpsExternalLongitude_Object((1,3,6,1,4,1,17713,24,5,0,12),_CnGpsExternalLongitude_Type())
cnGpsExternalLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalLongitude.setStatus(_A)
class _CnGpsInternalSignalQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5)))
_CnGpsInternalSignalQuality_Type.__name__=_C
_CnGpsInternalSignalQuality_Object=MibScalar
cnGpsInternalSignalQuality=_CnGpsInternalSignalQuality_Object((1,3,6,1,4,1,17713,24,5,0,13),_CnGpsInternalSignalQuality_Type())
cnGpsInternalSignalQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalSignalQuality.setStatus(_A)
class _CnGpsExternalSignalQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5)))
_CnGpsExternalSignalQuality_Type.__name__=_C
_CnGpsExternalSignalQuality_Object=MibScalar
cnGpsExternalSignalQuality=_CnGpsExternalSignalQuality_Object((1,3,6,1,4,1,17713,24,5,0,14),_CnGpsExternalSignalQuality_Type())
cnGpsExternalSignalQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalSignalQuality.setStatus(_A)
class _CnGpsInternalAntennaAltitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalAntennaAltitude_Type.__name__=_D
_CnGpsInternalAntennaAltitude_Object=MibScalar
cnGpsInternalAntennaAltitude=_CnGpsInternalAntennaAltitude_Object((1,3,6,1,4,1,17713,24,5,0,15),_CnGpsInternalAntennaAltitude_Type())
cnGpsInternalAntennaAltitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalAntennaAltitude.setStatus(_A)
class _CnGpsExternalAntennaAltitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalAntennaAltitude_Type.__name__=_D
_CnGpsExternalAntennaAltitude_Object=MibScalar
cnGpsExternalAntennaAltitude=_CnGpsExternalAntennaAltitude_Object((1,3,6,1,4,1,17713,24,5,0,16),_CnGpsExternalAntennaAltitude_Type())
cnGpsExternalAntennaAltitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalAntennaAltitude.setStatus(_A)
class _CnGpsInternalAntennaBaseAltitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalAntennaBaseAltitude_Type.__name__=_D
_CnGpsInternalAntennaBaseAltitude_Object=MibScalar
cnGpsInternalAntennaBaseAltitude=_CnGpsInternalAntennaBaseAltitude_Object((1,3,6,1,4,1,17713,24,5,0,17),_CnGpsInternalAntennaBaseAltitude_Type())
cnGpsInternalAntennaBaseAltitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalAntennaBaseAltitude.setStatus(_A)
class _CnGpsExternalAntennaBaseAltitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalAntennaBaseAltitude_Type.__name__=_D
_CnGpsExternalAntennaBaseAltitude_Object=MibScalar
cnGpsExternalAntennaBaseAltitude=_CnGpsExternalAntennaBaseAltitude_Object((1,3,6,1,4,1,17713,24,5,0,18),_CnGpsExternalAntennaBaseAltitude_Type())
cnGpsExternalAntennaBaseAltitude.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalAntennaBaseAltitude.setStatus(_A)
class _CnGpsInternalSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CnGpsInternalSelectionMode_Type.__name__=_C
_CnGpsInternalSelectionMode_Object=MibScalar
cnGpsInternalSelectionMode=_CnGpsInternalSelectionMode_Object((1,3,6,1,4,1,17713,24,5,0,19),_CnGpsInternalSelectionMode_Type())
cnGpsInternalSelectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalSelectionMode.setStatus(_A)
class _CnGpsExternalSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CnGpsExternalSelectionMode_Type.__name__=_C
_CnGpsExternalSelectionMode_Object=MibScalar
cnGpsExternalSelectionMode=_CnGpsExternalSelectionMode_Object((1,3,6,1,4,1,17713,24,5,0,20),_CnGpsExternalSelectionMode_Type())
cnGpsExternalSelectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalSelectionMode.setStatus(_A)
class _CnGpsInternalLocalizationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('two-D',2),(_S,3)))
_CnGpsInternalLocalizationType_Type.__name__=_C
_CnGpsInternalLocalizationType_Object=MibScalar
cnGpsInternalLocalizationType=_CnGpsInternalLocalizationType_Object((1,3,6,1,4,1,17713,24,5,0,21),_CnGpsInternalLocalizationType_Type())
cnGpsInternalLocalizationType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalLocalizationType.setStatus(_A)
class _CnGpsExternalLocalizationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('two-D',2),(_S,3)))
_CnGpsExternalLocalizationType_Type.__name__=_C
_CnGpsExternalLocalizationType_Object=MibScalar
cnGpsExternalLocalizationType=_CnGpsExternalLocalizationType_Object((1,3,6,1,4,1,17713,24,5,0,22),_CnGpsExternalLocalizationType_Type())
cnGpsExternalLocalizationType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalLocalizationType.setStatus(_A)
class _CnGpsInternalPdop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalPdop_Type.__name__=_D
_CnGpsInternalPdop_Object=MibScalar
cnGpsInternalPdop=_CnGpsInternalPdop_Object((1,3,6,1,4,1,17713,24,5,0,23),_CnGpsInternalPdop_Type())
cnGpsInternalPdop.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalPdop.setStatus(_A)
class _CnGpsExternalPdop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalPdop_Type.__name__=_D
_CnGpsExternalPdop_Object=MibScalar
cnGpsExternalPdop=_CnGpsExternalPdop_Object((1,3,6,1,4,1,17713,24,5,0,24),_CnGpsExternalPdop_Type())
cnGpsExternalPdop.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalPdop.setStatus(_A)
class _CnGpsInternalHdop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalHdop_Type.__name__=_D
_CnGpsInternalHdop_Object=MibScalar
cnGpsInternalHdop=_CnGpsInternalHdop_Object((1,3,6,1,4,1,17713,24,5,0,25),_CnGpsInternalHdop_Type())
cnGpsInternalHdop.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalHdop.setStatus(_A)
class _CnGpsExternalHdop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalHdop_Type.__name__=_D
_CnGpsExternalHdop_Object=MibScalar
cnGpsExternalHdop=_CnGpsExternalHdop_Object((1,3,6,1,4,1,17713,24,5,0,26),_CnGpsExternalHdop_Type())
cnGpsExternalHdop.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalHdop.setStatus(_A)
class _CnGpsInternalVdop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsInternalVdop_Type.__name__=_D
_CnGpsInternalVdop_Object=MibScalar
cnGpsInternalVdop=_CnGpsInternalVdop_Object((1,3,6,1,4,1,17713,24,5,0,27),_CnGpsInternalVdop_Type())
cnGpsInternalVdop.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalVdop.setStatus(_A)
class _CnGpsExternalVdop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnGpsExternalVdop_Type.__name__=_D
_CnGpsExternalVdop_Object=MibScalar
cnGpsExternalVdop=_CnGpsExternalVdop_Object((1,3,6,1,4,1,17713,24,5,0,28),_CnGpsExternalVdop_Type())
cnGpsExternalVdop.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalVdop.setStatus(_A)
class _CnGpsInternalSv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_CnGpsInternalSv_Type.__name__=_C
_CnGpsInternalSv_Object=MibScalar
cnGpsInternalSv=_CnGpsInternalSv_Object((1,3,6,1,4,1,17713,24,5,0,29),_CnGpsInternalSv_Type())
cnGpsInternalSv.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalSv.setStatus(_A)
class _CnGpsExternalSv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_CnGpsExternalSv_Type.__name__=_C
_CnGpsExternalSv_Object=MibScalar
cnGpsExternalSv=_CnGpsExternalSv_Object((1,3,6,1,4,1,17713,24,5,0,30),_CnGpsExternalSv_Type())
cnGpsExternalSv.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalSv.setStatus(_A)
class _CnGpsInternalSu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_CnGpsInternalSu_Type.__name__=_C
_CnGpsInternalSu_Object=MibScalar
cnGpsInternalSu=_CnGpsInternalSu_Object((1,3,6,1,4,1,17713,24,5,0,31),_CnGpsInternalSu_Type())
cnGpsInternalSu.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsInternalSu.setStatus(_A)
class _CnGpsExternalSu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_CnGpsExternalSu_Type.__name__=_C
_CnGpsExternalSu_Object=MibScalar
cnGpsExternalSu=_CnGpsExternalSu_Object((1,3,6,1,4,1,17713,24,5,0,32),_CnGpsExternalSu_Type())
cnGpsExternalSu.setMaxAccess(_B)
if mibBuilder.loadTexts:cnGpsExternalSu.setStatus(_A)
class _CnGpsExternalSourcePower_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('power-on',1),('power-off',2)))
_CnGpsExternalSourcePower_Type.__name__=_C
_CnGpsExternalSourcePower_Object=MibScalar
cnGpsExternalSourcePower=_CnGpsExternalSourcePower_Object((1,3,6,1,4,1,17713,24,5,0,33),_CnGpsExternalSourcePower_Type())
cnGpsExternalSourcePower.setMaxAccess(_E)
if mibBuilder.loadTexts:cnGpsExternalSourcePower.setStatus(_A)
cnGpsTrapMsg=NotificationType((1,3,6,1,4,1,17713,24,5,0,5))
cnGpsTrapMsg.setObjects((_H,_T))
if mibBuilder.loadTexts:cnGpsTrapMsg.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'cnGpsMib':cnGpsMib,'cnGpsObjects':cnGpsObjects,'cnGpsInternalSourceAdminStatus':cnGpsInternalSourceAdminStatus,'cnGpsExternalSourceAdminStatus':cnGpsExternalSourceAdminStatus,'cnGpsPortTable':cnGpsPortTable,'cnGpsPortEntry':cnGpsPortEntry,_I:cnGpsPortIndex,'cnGpsPortOutputAdminStatus':cnGpsPortOutputAdminStatus,_T:cnGpsSignalStatus,'cnGpsTrapMsg':cnGpsTrapMsg,'cnGpsSourcePowerCycle':cnGpsSourcePowerCycle,'cnGpsInternalTime':cnGpsInternalTime,'cnGpsExternalTime':cnGpsExternalTime,'cnGpsInternalLatitude':cnGpsInternalLatitude,'cnGpsExternalLatitude':cnGpsExternalLatitude,'cnGpsInternalLongitude':cnGpsInternalLongitude,'cnGpsExternalLongitude':cnGpsExternalLongitude,'cnGpsInternalSignalQuality':cnGpsInternalSignalQuality,'cnGpsExternalSignalQuality':cnGpsExternalSignalQuality,'cnGpsInternalAntennaAltitude':cnGpsInternalAntennaAltitude,'cnGpsExternalAntennaAltitude':cnGpsExternalAntennaAltitude,'cnGpsInternalAntennaBaseAltitude':cnGpsInternalAntennaBaseAltitude,'cnGpsExternalAntennaBaseAltitude':cnGpsExternalAntennaBaseAltitude,'cnGpsInternalSelectionMode':cnGpsInternalSelectionMode,'cnGpsExternalSelectionMode':cnGpsExternalSelectionMode,'cnGpsInternalLocalizationType':cnGpsInternalLocalizationType,'cnGpsExternalLocalizationType':cnGpsExternalLocalizationType,'cnGpsInternalPdop':cnGpsInternalPdop,'cnGpsExternalPdop':cnGpsExternalPdop,'cnGpsInternalHdop':cnGpsInternalHdop,'cnGpsExternalHdop':cnGpsExternalHdop,'cnGpsInternalVdop':cnGpsInternalVdop,'cnGpsExternalVdop':cnGpsExternalVdop,'cnGpsInternalSv':cnGpsInternalSv,'cnGpsExternalSv':cnGpsExternalSv,'cnGpsInternalSu':cnGpsInternalSu,'cnGpsExternalSu':cnGpsExternalSu,'cnGpsExternalSourcePower':cnGpsExternalSourcePower})