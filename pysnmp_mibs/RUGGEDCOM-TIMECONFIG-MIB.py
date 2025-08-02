_M='rcDSTRule'
_L='rcLeapSecPending'
_K='rcCurrentUTCOfst'
_J='rcDSTOfst'
_I='rcTimeAndDate'
_H='rcTimeSource'
_G='seconds'
_F='DisplayString'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='RUGGEDCOM-TIMECONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruggedcomMgmt,=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','TextualConvention','TruthValue')
rcTimeConfig=ModuleIdentity((1,3,6,1,4,1,15004,4,11))
if mibBuilder.loadTexts:rcTimeConfig.setRevisions(('2015-09-28 13:00',))
class RcTimeSyncStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('notPresent',1),('disabled',2),('locked',3),('searching',4),('aquiring',5),('holdover',6),('parity',7),('decoder',8),('shortckt',9),('cfgfailure',10)))
_RcTimeConfigBase_ObjectIdentity=ObjectIdentity
rcTimeConfigBase=_RcTimeConfigBase_ObjectIdentity((1,3,6,1,4,1,15004,4,11,1))
class _RcTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('irigb',2),('gps',3),('ieee1588',4),('ntp',5),('localclk',6)))
_RcTimeSource_Type.__name__=_E
_RcTimeSource_Object=MibScalar
rcTimeSource=_RcTimeSource_Object((1,3,6,1,4,1,15004,4,11,1,1),_RcTimeSource_Type())
rcTimeSource.setMaxAccess(_C)
if mibBuilder.loadTexts:rcTimeSource.setStatus(_A)
_RcTimeAndDate_Type=DateAndTime
_RcTimeAndDate_Object=MibScalar
rcTimeAndDate=_RcTimeAndDate_Object((1,3,6,1,4,1,15004,4,11,1,2),_RcTimeAndDate_Type())
rcTimeAndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcTimeAndDate.setStatus(_A)
class _RcDSTOfst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
_RcDSTOfst_Type.__name__=_D
_RcDSTOfst_Object=MibScalar
rcDSTOfst=_RcDSTOfst_Object((1,3,6,1,4,1,15004,4,11,1,3),_RcDSTOfst_Type())
rcDSTOfst.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDSTOfst.setStatus(_A)
if mibBuilder.loadTexts:rcDSTOfst.setUnits(_G)
class _RcCurrentUTCOfst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCurrentUTCOfst_Type.__name__=_D
_RcCurrentUTCOfst_Object=MibScalar
rcCurrentUTCOfst=_RcCurrentUTCOfst_Object((1,3,6,1,4,1,15004,4,11,1,4),_RcCurrentUTCOfst_Type())
rcCurrentUTCOfst.setMaxAccess(_C)
if mibBuilder.loadTexts:rcCurrentUTCOfst.setStatus(_A)
if mibBuilder.loadTexts:rcCurrentUTCOfst.setUnits(_G)
_RcLeapSecPending_Type=TruthValue
_RcLeapSecPending_Object=MibScalar
rcLeapSecPending=_RcLeapSecPending_Object((1,3,6,1,4,1,15004,4,11,1,5),_RcLeapSecPending_Type())
rcLeapSecPending.setMaxAccess(_C)
if mibBuilder.loadTexts:rcLeapSecPending.setStatus(_A)
class _RcDSTRule_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcDSTRule_Type.__name__=_F
_RcDSTRule_Object=MibScalar
rcDSTRule=_RcDSTRule_Object((1,3,6,1,4,1,15004,4,11,1,6),_RcDSTRule_Type())
rcDSTRule.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDSTRule.setStatus(_A)
_RcTimeConfigConformance_ObjectIdentity=ObjectIdentity
rcTimeConfigConformance=_RcTimeConfigConformance_ObjectIdentity((1,3,6,1,4,1,15004,4,11,3))
_RcTimeConfigGroups_ObjectIdentity=ObjectIdentity
rcTimeConfigGroups=_RcTimeConfigGroups_ObjectIdentity((1,3,6,1,4,1,15004,4,11,3,2))
rcTimeConfigBaseGroup=ObjectGroup((1,3,6,1,4,1,15004,4,11,3,2,1))
rcTimeConfigBaseGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:rcTimeConfigBaseGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RcTimeSyncStatus':RcTimeSyncStatus,'rcTimeConfig':rcTimeConfig,'rcTimeConfigBase':rcTimeConfigBase,_H:rcTimeSource,_I:rcTimeAndDate,_J:rcDSTOfst,_K:rcCurrentUTCOfst,_L:rcLeapSecPending,_M:rcDSTRule,'rcTimeConfigConformance':rcTimeConfigConformance,'rcTimeConfigGroups':rcTimeConfigGroups,'rcTimeConfigBaseGroup':rcTimeConfigBaseGroup})