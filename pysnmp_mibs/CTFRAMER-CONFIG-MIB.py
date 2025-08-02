_H='ifIndex'
_G='IF-MIB'
_F='ctIfPortPortNumber'
_E='CTIF-EXT-MIB'
_D='off'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFramerConfig,ctIfPortPortNumber=mibBuilder.importSymbols(_E,'ctFramerConfig',_F)
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtFramerBaseConfig_ObjectIdentity=ObjectIdentity
ctFramerBaseConfig=_CtFramerBaseConfig_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,9,1))
_CtFramerConfigTable_Object=MibTable
ctFramerConfigTable=_CtFramerConfigTable_Object((1,3,6,1,4,1,52,4,3,3,9,1,1))
if mibBuilder.loadTexts:ctFramerConfigTable.setStatus(_A)
_CtFramerConfigEntry_Object=MibTableRow
ctFramerConfigEntry=_CtFramerConfigEntry_Object((1,3,6,1,4,1,52,4,3,3,9,1,1,1))
ctFramerConfigEntry.setIndexNames((0,_G,_H),(0,_E,_F))
if mibBuilder.loadTexts:ctFramerConfigEntry.setStatus(_A)
class _CtFramerStatsConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_D,2)))
_CtFramerStatsConfig_Type.__name__=_B
_CtFramerStatsConfig_Object=MibTableColumn
ctFramerStatsConfig=_CtFramerStatsConfig_Object((1,3,6,1,4,1,52,4,3,3,9,1,1,1,1),_CtFramerStatsConfig_Type())
ctFramerStatsConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFramerStatsConfig.setStatus(_A)
class _CtFramerAlarmsConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_D,2)))
_CtFramerAlarmsConfig_Type.__name__=_B
_CtFramerAlarmsConfig_Object=MibTableColumn
ctFramerAlarmsConfig=_CtFramerAlarmsConfig_Object((1,3,6,1,4,1,52,4,3,3,9,1,1,1,2),_CtFramerAlarmsConfig_Type())
ctFramerAlarmsConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFramerAlarmsConfig.setStatus(_A)
class _CtFramerMediumConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_CtFramerMediumConfig_Type.__name__=_B
_CtFramerMediumConfig_Object=MibTableColumn
ctFramerMediumConfig=_CtFramerMediumConfig_Object((1,3,6,1,4,1,52,4,3,3,9,1,1,1,3),_CtFramerMediumConfig_Type())
ctFramerMediumConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFramerMediumConfig.setStatus(_A)
class _CtFramerIdleCellsConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('unassigned',2)))
_CtFramerIdleCellsConfig_Type.__name__=_B
_CtFramerIdleCellsConfig_Object=MibTableColumn
ctFramerIdleCellsConfig=_CtFramerIdleCellsConfig_Object((1,3,6,1,4,1,52,4,3,3,9,1,1,1,4),_CtFramerIdleCellsConfig_Type())
ctFramerIdleCellsConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFramerIdleCellsConfig.setStatus(_A)
class _CtFramerCellPayScramConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_D,2)))
_CtFramerCellPayScramConfig_Type.__name__=_B
_CtFramerCellPayScramConfig_Object=MibTableColumn
ctFramerCellPayScramConfig=_CtFramerCellPayScramConfig_Object((1,3,6,1,4,1,52,4,3,3,9,1,1,1,5),_CtFramerCellPayScramConfig_Type())
ctFramerCellPayScramConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFramerCellPayScramConfig.setStatus(_A)
_CtFramerSonetConfig_ObjectIdentity=ObjectIdentity
ctFramerSonetConfig=_CtFramerSonetConfig_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,9,2))
_CtFramerDS3Config_ObjectIdentity=ObjectIdentity
ctFramerDS3Config=_CtFramerDS3Config_ObjectIdentity((1,3,6,1,4,1,52,4,3,3,9,3))
mibBuilder.exportSymbols('CTFRAMER-CONFIG-MIB',**{'ctFramerBaseConfig':ctFramerBaseConfig,'ctFramerConfigTable':ctFramerConfigTable,'ctFramerConfigEntry':ctFramerConfigEntry,'ctFramerStatsConfig':ctFramerStatsConfig,'ctFramerAlarmsConfig':ctFramerAlarmsConfig,'ctFramerMediumConfig':ctFramerMediumConfig,'ctFramerIdleCellsConfig':ctFramerIdleCellsConfig,'ctFramerCellPayScramConfig':ctFramerCellPayScramConfig,'ctFramerSonetConfig':ctFramerSonetConfig,'ctFramerDS3Config':ctFramerDS3Config})