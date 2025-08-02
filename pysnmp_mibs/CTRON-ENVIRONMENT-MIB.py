_S='psEnvSlotID'
_R='boardEnvSlotID'
_Q='testingMode'
_P='fullSpeed'
_O='autoMode'
_N='testing'
_M='chEnvFanID'
_L='read-write'
_K='cool'
_J='cold'
_I='CTRON-ENVIRONMENT-MIB'
_H='hot'
_G='warm'
_F='inoperative'
_E='normal'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctenv,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctenv')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_ChEnv_ObjectIdentity=ObjectIdentity
chEnv=_ChEnv_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,8,1))
_ChEnvAmbientTemp_Type=Integer32
_ChEnvAmbientTemp_Object=MibScalar
chEnvAmbientTemp=_ChEnvAmbientTemp_Object((1,3,6,1,4,1,52,4,1,1,8,1,1),_ChEnvAmbientTemp_Type())
chEnvAmbientTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvAmbientTemp.setStatus(_A)
class _ChEnvAmbientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_J,2),(_K,3),(_E,4),(_G,5),(_H,6),(_F,7)))
_ChEnvAmbientStatus_Type.__name__=_C
_ChEnvAmbientStatus_Object=MibScalar
chEnvAmbientStatus=_ChEnvAmbientStatus_Object((1,3,6,1,4,1,52,4,1,1,8,1,2),_ChEnvAmbientStatus_Type())
chEnvAmbientStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvAmbientStatus.setStatus(_A)
_ChEnvHumidity_Type=Integer32
_ChEnvHumidity_Object=MibScalar
chEnvHumidity=_ChEnvHumidity_Object((1,3,6,1,4,1,52,4,1,1,8,1,3),_ChEnvHumidity_Type())
chEnvHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvHumidity.setStatus(_A)
class _ChEnvHumidityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('dry',2),(_E,3),('moist',4),(_F,5)))
_ChEnvHumidityStatus_Type.__name__=_C
_ChEnvHumidityStatus_Object=MibScalar
chEnvHumidityStatus=_ChEnvHumidityStatus_Object((1,3,6,1,4,1,52,4,1,1,8,1,4),_ChEnvHumidityStatus_Type())
chEnvHumidityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvHumidityStatus.setStatus(_A)
_ChEnvAmbientHot_Type=Integer32
_ChEnvAmbientHot_Object=MibScalar
chEnvAmbientHot=_ChEnvAmbientHot_Object((1,3,6,1,4,1,52,4,1,1,8,1,5),_ChEnvAmbientHot_Type())
chEnvAmbientHot.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvAmbientHot.setStatus(_A)
_ChEnvAmbientWarm_Type=Integer32
_ChEnvAmbientWarm_Object=MibScalar
chEnvAmbientWarm=_ChEnvAmbientWarm_Object((1,3,6,1,4,1,52,4,1,1,8,1,6),_ChEnvAmbientWarm_Type())
chEnvAmbientWarm.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvAmbientWarm.setStatus(_A)
_ChEnvAmbientCool_Type=Integer32
_ChEnvAmbientCool_Object=MibScalar
chEnvAmbientCool=_ChEnvAmbientCool_Object((1,3,6,1,4,1,52,4,1,1,8,1,7),_ChEnvAmbientCool_Type())
chEnvAmbientCool.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvAmbientCool.setStatus(_A)
_ChEnvAmbientCold_Type=Integer32
_ChEnvAmbientCold_Object=MibScalar
chEnvAmbientCold=_ChEnvAmbientCold_Object((1,3,6,1,4,1,52,4,1,1,8,1,8),_ChEnvAmbientCold_Type())
chEnvAmbientCold.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvAmbientCold.setStatus(_A)
_ChEnvHumidityMoist_Type=Integer32
_ChEnvHumidityMoist_Object=MibScalar
chEnvHumidityMoist=_ChEnvHumidityMoist_Object((1,3,6,1,4,1,52,4,1,1,8,1,9),_ChEnvHumidityMoist_Type())
chEnvHumidityMoist.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvHumidityMoist.setStatus(_A)
_ChEnvHumidityDry_Type=Integer32
_ChEnvHumidityDry_Object=MibScalar
chEnvHumidityDry=_ChEnvHumidityDry_Object((1,3,6,1,4,1,52,4,1,1,8,1,10),_ChEnvHumidityDry_Type())
chEnvHumidityDry.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvHumidityDry.setStatus(_A)
class _ChEnvNumFans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ChEnvNumFans_Type.__name__=_C
_ChEnvNumFans_Object=MibScalar
chEnvNumFans=_ChEnvNumFans_Object((1,3,6,1,4,1,52,4,1,1,8,1,11),_ChEnvNumFans_Type())
chEnvNumFans.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvNumFans.setStatus(_A)
_ChEnvFanTable_Object=MibTable
chEnvFanTable=_ChEnvFanTable_Object((1,3,6,1,4,1,52,4,1,1,8,1,12))
if mibBuilder.loadTexts:chEnvFanTable.setStatus(_A)
_ChEnvFanEntry_Object=MibTableRow
chEnvFanEntry=_ChEnvFanEntry_Object((1,3,6,1,4,1,52,4,1,1,8,1,12,1))
chEnvFanEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:chEnvFanEntry.setStatus(_A)
_ChEnvFanID_Type=Integer32
_ChEnvFanID_Object=MibTableColumn
chEnvFanID=_ChEnvFanID_Object((1,3,6,1,4,1,52,4,1,1,8,1,12,1,1),_ChEnvFanID_Type())
chEnvFanID.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvFanID.setStatus(_A)
class _ChEnvFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_E,2),(_N,3),('slow',4),(_F,5),('off',6)))
_ChEnvFanStatus_Type.__name__=_C
_ChEnvFanStatus_Object=MibTableColumn
chEnvFanStatus=_ChEnvFanStatus_Object((1,3,6,1,4,1,52,4,1,1,8,1,12,1,2),_ChEnvFanStatus_Type())
chEnvFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvFanStatus.setStatus(_A)
class _ChEnvFanAdmin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3)))
_ChEnvFanAdmin_Type.__name__=_C
_ChEnvFanAdmin_Object=MibTableColumn
chEnvFanAdmin=_ChEnvFanAdmin_Object((1,3,6,1,4,1,52,4,1,1,8,1,12,1,3),_ChEnvFanAdmin_Type())
chEnvFanAdmin.setMaxAccess(_L)
if mibBuilder.loadTexts:chEnvFanAdmin.setStatus(_A)
_ChEnvFanSpeed_Type=Integer32
_ChEnvFanSpeed_Object=MibTableColumn
chEnvFanSpeed=_ChEnvFanSpeed_Object((1,3,6,1,4,1,52,4,1,1,8,1,12,1,4),_ChEnvFanSpeed_Type())
chEnvFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:chEnvFanSpeed.setStatus(_A)
_BoardEnv_ObjectIdentity=ObjectIdentity
boardEnv=_BoardEnv_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,8,2))
_BoardEnvSlotTable_Object=MibTable
boardEnvSlotTable=_BoardEnvSlotTable_Object((1,3,6,1,4,1,52,4,1,1,8,2,1))
if mibBuilder.loadTexts:boardEnvSlotTable.setStatus(_A)
_BoardEnvSlotEntry_Object=MibTableRow
boardEnvSlotEntry=_BoardEnvSlotEntry_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1))
boardEnvSlotEntry.setIndexNames((0,_I,_R))
if mibBuilder.loadTexts:boardEnvSlotEntry.setStatus(_A)
_BoardEnvSlotID_Type=Integer32
_BoardEnvSlotID_Object=MibTableColumn
boardEnvSlotID=_BoardEnvSlotID_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,1),_BoardEnvSlotID_Type())
boardEnvSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvSlotID.setStatus(_A)
_BoardEnvTemp_Type=Integer32
_BoardEnvTemp_Object=MibTableColumn
boardEnvTemp=_BoardEnvTemp_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,2),_BoardEnvTemp_Type())
boardEnvTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTemp.setStatus(_A)
class _BoardEnvTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_J,2),(_K,3),(_E,4),(_G,5),(_H,6),(_F,7)))
_BoardEnvTempStatus_Type.__name__=_C
_BoardEnvTempStatus_Object=MibTableColumn
boardEnvTempStatus=_BoardEnvTempStatus_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,3),_BoardEnvTempStatus_Type())
boardEnvTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempStatus.setStatus(_A)
class _BoardEnvTempRelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3),(_H,4),(_F,5)))
_BoardEnvTempRelStatus_Type.__name__=_C
_BoardEnvTempRelStatus_Object=MibTableColumn
boardEnvTempRelStatus=_BoardEnvTempRelStatus_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,4),_BoardEnvTempRelStatus_Type())
boardEnvTempRelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempRelStatus.setStatus(_A)
class _BoardEnvShutdownAdmin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_BoardEnvShutdownAdmin_Type.__name__=_C
_BoardEnvShutdownAdmin_Object=MibTableColumn
boardEnvShutdownAdmin=_BoardEnvShutdownAdmin_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,5),_BoardEnvShutdownAdmin_Type())
boardEnvShutdownAdmin.setMaxAccess(_L)
if mibBuilder.loadTexts:boardEnvShutdownAdmin.setStatus(_A)
_BoardEnvTempHot_Type=Integer32
_BoardEnvTempHot_Object=MibTableColumn
boardEnvTempHot=_BoardEnvTempHot_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,6),_BoardEnvTempHot_Type())
boardEnvTempHot.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempHot.setStatus(_A)
_BoardEnvTempWarm_Type=Integer32
_BoardEnvTempWarm_Object=MibTableColumn
boardEnvTempWarm=_BoardEnvTempWarm_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,7),_BoardEnvTempWarm_Type())
boardEnvTempWarm.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempWarm.setStatus(_A)
_BoardEnvTempCool_Type=Integer32
_BoardEnvTempCool_Object=MibTableColumn
boardEnvTempCool=_BoardEnvTempCool_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,8),_BoardEnvTempCool_Type())
boardEnvTempCool.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempCool.setStatus(_A)
_BoardEnvTempCold_Type=Integer32
_BoardEnvTempCold_Object=MibTableColumn
boardEnvTempCold=_BoardEnvTempCold_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,9),_BoardEnvTempCold_Type())
boardEnvTempCold.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempCold.setStatus(_A)
_BoardEnvTempRelHot_Type=Integer32
_BoardEnvTempRelHot_Object=MibTableColumn
boardEnvTempRelHot=_BoardEnvTempRelHot_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,10),_BoardEnvTempRelHot_Type())
boardEnvTempRelHot.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempRelHot.setStatus(_A)
_BoardEnvTempRelWarm_Type=Integer32
_BoardEnvTempRelWarm_Object=MibTableColumn
boardEnvTempRelWarm=_BoardEnvTempRelWarm_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,11),_BoardEnvTempRelWarm_Type())
boardEnvTempRelWarm.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempRelWarm.setStatus(_A)
_BoardEnvTempMaxFanRelHot_Type=Integer32
_BoardEnvTempMaxFanRelHot_Object=MibTableColumn
boardEnvTempMaxFanRelHot=_BoardEnvTempMaxFanRelHot_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,12),_BoardEnvTempMaxFanRelHot_Type())
boardEnvTempMaxFanRelHot.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempMaxFanRelHot.setStatus(_A)
_BoardEnvTempMaxFanRelWarm_Type=Integer32
_BoardEnvTempMaxFanRelWarm_Object=MibTableColumn
boardEnvTempMaxFanRelWarm=_BoardEnvTempMaxFanRelWarm_Object((1,3,6,1,4,1,52,4,1,1,8,2,1,1,13),_BoardEnvTempMaxFanRelWarm_Type())
boardEnvTempMaxFanRelWarm.setMaxAccess(_B)
if mibBuilder.loadTexts:boardEnvTempMaxFanRelWarm.setStatus(_A)
_PsEnv_ObjectIdentity=ObjectIdentity
psEnv=_PsEnv_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,8,3))
_PsEnvSlotTable_Object=MibTable
psEnvSlotTable=_PsEnvSlotTable_Object((1,3,6,1,4,1,52,4,1,1,8,3,1))
if mibBuilder.loadTexts:psEnvSlotTable.setStatus(_A)
_PsEnvSlotEntry_Object=MibTableRow
psEnvSlotEntry=_PsEnvSlotEntry_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1))
psEnvSlotEntry.setIndexNames((0,_I,_S))
if mibBuilder.loadTexts:psEnvSlotEntry.setStatus(_A)
_PsEnvSlotID_Type=Integer32
_PsEnvSlotID_Object=MibTableColumn
psEnvSlotID=_PsEnvSlotID_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,1),_PsEnvSlotID_Type())
psEnvSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvSlotID.setStatus(_A)
_PsEnvTemp_Type=Integer32
_PsEnvTemp_Object=MibTableColumn
psEnvTemp=_PsEnvTemp_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,2),_PsEnvTemp_Type())
psEnvTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvTemp.setStatus(_A)
class _PsEnvTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_J,2),(_K,3),(_E,4),(_G,5),(_H,6),(_F,7)))
_PsEnvTempStatus_Type.__name__=_C
_PsEnvTempStatus_Object=MibTableColumn
psEnvTempStatus=_PsEnvTempStatus_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,3),_PsEnvTempStatus_Type())
psEnvTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvTempStatus.setStatus(_A)
_PsEnvTempHot_Type=Integer32
_PsEnvTempHot_Object=MibTableColumn
psEnvTempHot=_PsEnvTempHot_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,4),_PsEnvTempHot_Type())
psEnvTempHot.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvTempHot.setStatus(_A)
_PsEnvTempWarm_Type=Integer32
_PsEnvTempWarm_Object=MibTableColumn
psEnvTempWarm=_PsEnvTempWarm_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,5),_PsEnvTempWarm_Type())
psEnvTempWarm.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvTempWarm.setStatus(_A)
_PsEnvTempCool_Type=Integer32
_PsEnvTempCool_Object=MibTableColumn
psEnvTempCool=_PsEnvTempCool_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,6),_PsEnvTempCool_Type())
psEnvTempCool.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvTempCool.setStatus(_A)
_PsEnvTempCold_Type=Integer32
_PsEnvTempCold_Object=MibTableColumn
psEnvTempCold=_PsEnvTempCold_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,7),_PsEnvTempCold_Type())
psEnvTempCold.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvTempCold.setStatus(_A)
class _PsEnvFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_E,2),(_N,3),('slow',4),(_F,5),('off',6)))
_PsEnvFanStatus_Type.__name__=_C
_PsEnvFanStatus_Object=MibTableColumn
psEnvFanStatus=_PsEnvFanStatus_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,8),_PsEnvFanStatus_Type())
psEnvFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvFanStatus.setStatus(_A)
class _PsEnvFanAdmin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3)))
_PsEnvFanAdmin_Type.__name__=_C
_PsEnvFanAdmin_Object=MibTableColumn
psEnvFanAdmin=_PsEnvFanAdmin_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,9),_PsEnvFanAdmin_Type())
psEnvFanAdmin.setMaxAccess(_L)
if mibBuilder.loadTexts:psEnvFanAdmin.setStatus(_A)
_PsEnvFanSpeed_Type=Integer32
_PsEnvFanSpeed_Object=MibTableColumn
psEnvFanSpeed=_PsEnvFanSpeed_Object((1,3,6,1,4,1,52,4,1,1,8,3,1,1,10),_PsEnvFanSpeed_Type())
psEnvFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:psEnvFanSpeed.setStatus(_A)
_BbuEnv_ObjectIdentity=ObjectIdentity
bbuEnv=_BbuEnv_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,8,4))
mibBuilder.exportSymbols(_I,**{'chEnv':chEnv,'chEnvAmbientTemp':chEnvAmbientTemp,'chEnvAmbientStatus':chEnvAmbientStatus,'chEnvHumidity':chEnvHumidity,'chEnvHumidityStatus':chEnvHumidityStatus,'chEnvAmbientHot':chEnvAmbientHot,'chEnvAmbientWarm':chEnvAmbientWarm,'chEnvAmbientCool':chEnvAmbientCool,'chEnvAmbientCold':chEnvAmbientCold,'chEnvHumidityMoist':chEnvHumidityMoist,'chEnvHumidityDry':chEnvHumidityDry,'chEnvNumFans':chEnvNumFans,'chEnvFanTable':chEnvFanTable,'chEnvFanEntry':chEnvFanEntry,_M:chEnvFanID,'chEnvFanStatus':chEnvFanStatus,'chEnvFanAdmin':chEnvFanAdmin,'chEnvFanSpeed':chEnvFanSpeed,'boardEnv':boardEnv,'boardEnvSlotTable':boardEnvSlotTable,'boardEnvSlotEntry':boardEnvSlotEntry,_R:boardEnvSlotID,'boardEnvTemp':boardEnvTemp,'boardEnvTempStatus':boardEnvTempStatus,'boardEnvTempRelStatus':boardEnvTempRelStatus,'boardEnvShutdownAdmin':boardEnvShutdownAdmin,'boardEnvTempHot':boardEnvTempHot,'boardEnvTempWarm':boardEnvTempWarm,'boardEnvTempCool':boardEnvTempCool,'boardEnvTempCold':boardEnvTempCold,'boardEnvTempRelHot':boardEnvTempRelHot,'boardEnvTempRelWarm':boardEnvTempRelWarm,'boardEnvTempMaxFanRelHot':boardEnvTempMaxFanRelHot,'boardEnvTempMaxFanRelWarm':boardEnvTempMaxFanRelWarm,'psEnv':psEnv,'psEnvSlotTable':psEnvSlotTable,'psEnvSlotEntry':psEnvSlotEntry,_S:psEnvSlotID,'psEnvTemp':psEnvTemp,'psEnvTempStatus':psEnvTempStatus,'psEnvTempHot':psEnvTempHot,'psEnvTempWarm':psEnvTempWarm,'psEnvTempCool':psEnvTempCool,'psEnvTempCold':psEnvTempCold,'psEnvFanStatus':psEnvFanStatus,'psEnvFanAdmin':psEnvFanAdmin,'psEnvFanSpeed':psEnvFanSpeed,'bbuEnv':bbuEnv})