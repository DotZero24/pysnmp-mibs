_V='hpicfDebugTimeStampGroup'
_U='hpicfDebugTimeStamp'
_T='hpicfDebugDestPersistent'
_S='hpicfDebugDestStatus'
_R='hpicfDebugLogPersistent'
_Q='hpicfDebugLogLevel'
_P='hpicfDebugLogStatus'
_O='hpicfDebugLogContainedIn'
_N='hpicfDebugLogDescr'
_M='hpicfDebugDestIndex'
_L='HpicfDebugLogLevels'
_K='read-only'
_J='not-accessible'
_I='hpicfDebugLogIndex'
_H='TruthValue'
_G='DisplayString'
_F='hpicfDebugDestGroup'
_E='hpicfDebugLogGroup'
_D='Integer32'
_C='read-write'
_B='HP-ICF-DEBUGLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpicfDebugLog,=mibBuilder.importSymbols('HP-ICF-OID','hpicfDebugLog')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention',_H)
hpicfDebugLogMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,64,1))
if mibBuilder.loadTexts:hpicfDebugLogMib.setRevisions(('2017-07-04 00:00','2016-03-18 00:00','2016-02-17 00:00','2009-09-22 00:00'))
class HpicfDebugDestType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('syslog',1),('buffer',2)))
class HpicfDebugLogLevels(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('quiet',0),('fatal',1),('error',2),('info',3),('verbose',4),('debug',5),('debug2',6),('debug3',7)))
_HpicfDebugLogObjects_ObjectIdentity=ObjectIdentity
hpicfDebugLogObjects=_HpicfDebugLogObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1))
_HpicfDebugLogControlTable_Object=MibTable
hpicfDebugLogControlTable=_HpicfDebugLogControlTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,1))
if mibBuilder.loadTexts:hpicfDebugLogControlTable.setStatus(_A)
_HpicfDebugLogControlEntry_Object=MibTableRow
hpicfDebugLogControlEntry=_HpicfDebugLogControlEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,1,1))
hpicfDebugLogControlEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hpicfDebugLogControlEntry.setStatus(_A)
class _HpicfDebugLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpicfDebugLogIndex_Type.__name__=_D
_HpicfDebugLogIndex_Object=MibTableColumn
hpicfDebugLogIndex=_HpicfDebugLogIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,1,1,1),_HpicfDebugLogIndex_Type())
hpicfDebugLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfDebugLogIndex.setStatus(_A)
class _HpicfDebugLogDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfDebugLogDescr_Type.__name__=_G
_HpicfDebugLogDescr_Object=MibTableColumn
hpicfDebugLogDescr=_HpicfDebugLogDescr_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,1,1,2),_HpicfDebugLogDescr_Type())
hpicfDebugLogDescr.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfDebugLogDescr.setStatus(_A)
class _HpicfDebugLogContainedIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpicfDebugLogContainedIn_Type.__name__=_D
_HpicfDebugLogContainedIn_Object=MibTableColumn
hpicfDebugLogContainedIn=_HpicfDebugLogContainedIn_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,1,1,3),_HpicfDebugLogContainedIn_Type())
hpicfDebugLogContainedIn.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfDebugLogContainedIn.setStatus(_A)
_HpicfDebugLogStatus_Type=TruthValue
_HpicfDebugLogStatus_Object=MibTableColumn
hpicfDebugLogStatus=_HpicfDebugLogStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,1,1,4),_HpicfDebugLogStatus_Type())
hpicfDebugLogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDebugLogStatus.setStatus(_A)
_HpicfDebugLogPersistent_Type=TruthValue
_HpicfDebugLogPersistent_Object=MibTableColumn
hpicfDebugLogPersistent=_HpicfDebugLogPersistent_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,1,1,5),_HpicfDebugLogPersistent_Type())
hpicfDebugLogPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDebugLogPersistent.setStatus(_A)
class _HpicfDebugLogLevel_Type(HpicfDebugLogLevels):defaultValue=3
_HpicfDebugLogLevel_Type.__name__=_L
_HpicfDebugLogLevel_Object=MibScalar
hpicfDebugLogLevel=_HpicfDebugLogLevel_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,2),_HpicfDebugLogLevel_Type())
hpicfDebugLogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDebugLogLevel.setStatus(_A)
_HpicfDebugDestControlTable_Object=MibTable
hpicfDebugDestControlTable=_HpicfDebugDestControlTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,3))
if mibBuilder.loadTexts:hpicfDebugDestControlTable.setStatus(_A)
_HpicfDebugDestControlEntry_Object=MibTableRow
hpicfDebugDestControlEntry=_HpicfDebugDestControlEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,3,1))
hpicfDebugDestControlEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:hpicfDebugDestControlEntry.setStatus(_A)
_HpicfDebugDestIndex_Type=HpicfDebugDestType
_HpicfDebugDestIndex_Object=MibTableColumn
hpicfDebugDestIndex=_HpicfDebugDestIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,3,1,1),_HpicfDebugDestIndex_Type())
hpicfDebugDestIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfDebugDestIndex.setStatus(_A)
_HpicfDebugDestStatus_Type=TruthValue
_HpicfDebugDestStatus_Object=MibTableColumn
hpicfDebugDestStatus=_HpicfDebugDestStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,3,1,2),_HpicfDebugDestStatus_Type())
hpicfDebugDestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDebugDestStatus.setStatus(_A)
_HpicfDebugDestPersistent_Type=TruthValue
_HpicfDebugDestPersistent_Object=MibTableColumn
hpicfDebugDestPersistent=_HpicfDebugDestPersistent_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,3,1,3),_HpicfDebugDestPersistent_Type())
hpicfDebugDestPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDebugDestPersistent.setStatus(_A)
class _HpicfDebugTimeStamp_Type(TruthValue):defaultValue=2
_HpicfDebugTimeStamp_Type.__name__=_H
_HpicfDebugTimeStamp_Object=MibScalar
hpicfDebugTimeStamp=_HpicfDebugTimeStamp_Object((1,3,6,1,4,1,11,2,14,11,5,1,64,1,1,4),_HpicfDebugTimeStamp_Type())
hpicfDebugTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDebugTimeStamp.setStatus(_A)
_HpicfDebugLogConformance_ObjectIdentity=ObjectIdentity
hpicfDebugLogConformance=_HpicfDebugLogConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2))
_HpicfDebugLogCompliances_ObjectIdentity=ObjectIdentity
hpicfDebugLogCompliances=_HpicfDebugLogCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,1))
_HpicfDebugLogGroups_ObjectIdentity=ObjectIdentity
hpicfDebugLogGroups=_HpicfDebugLogGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,2))
_HpicfDebugDestGroups_ObjectIdentity=ObjectIdentity
hpicfDebugDestGroups=_HpicfDebugDestGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,3))
_HpicfDebugTimeStampGroups_ObjectIdentity=ObjectIdentity
hpicfDebugTimeStampGroups=_HpicfDebugTimeStampGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,4))
hpicfDebugLogGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,2,1))
hpicfDebugLogGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpicfDebugLogGroup.setStatus(_A)
hpicfDebugDestGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,3,1))
hpicfDebugDestGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:hpicfDebugDestGroup.setStatus(_A)
hpicfDebugTimeStampGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,4,1))
hpicfDebugTimeStampGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:hpicfDebugTimeStampGroup.setStatus(_A)
hpicfDebugLogCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,1,1))
hpicfDebugLogCompliance.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:hpicfDebugLogCompliance.setStatus('deprecated')
hpicfDebugLogCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,64,1,2,1,2))
hpicfDebugLogCompliance1.setObjects(*((_B,_E),(_B,_F),(_B,_V)))
if mibBuilder.loadTexts:hpicfDebugLogCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpicfDebugDestType':HpicfDebugDestType,_L:HpicfDebugLogLevels,'hpicfDebugLogMib':hpicfDebugLogMib,'hpicfDebugLogObjects':hpicfDebugLogObjects,'hpicfDebugLogControlTable':hpicfDebugLogControlTable,'hpicfDebugLogControlEntry':hpicfDebugLogControlEntry,_I:hpicfDebugLogIndex,_N:hpicfDebugLogDescr,_O:hpicfDebugLogContainedIn,_P:hpicfDebugLogStatus,_R:hpicfDebugLogPersistent,_Q:hpicfDebugLogLevel,'hpicfDebugDestControlTable':hpicfDebugDestControlTable,'hpicfDebugDestControlEntry':hpicfDebugDestControlEntry,_M:hpicfDebugDestIndex,_S:hpicfDebugDestStatus,_T:hpicfDebugDestPersistent,_U:hpicfDebugTimeStamp,'hpicfDebugLogConformance':hpicfDebugLogConformance,'hpicfDebugLogCompliances':hpicfDebugLogCompliances,'hpicfDebugLogCompliance':hpicfDebugLogCompliance,'hpicfDebugLogCompliance1':hpicfDebugLogCompliance1,'hpicfDebugLogGroups':hpicfDebugLogGroups,_E:hpicfDebugLogGroup,'hpicfDebugDestGroups':hpicfDebugDestGroups,_F:hpicfDebugDestGroup,'hpicfDebugTimeStampGroups':hpicfDebugTimeStampGroups,_V:hpicfDebugTimeStampGroup})