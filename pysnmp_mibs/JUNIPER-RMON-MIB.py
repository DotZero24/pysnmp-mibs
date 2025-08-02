_I='jnxRmonAlarmGetFailReason'
_H='jnxRmonAlarmEntry'
_G='JUNIPER-RMON-MIB'
_F='Integer32'
_E='alarmVariable'
_D='alarmIndex'
_C='read-only'
_B='RMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,jnxRmonTraps=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs','jnxRmonTraps')
alarmEntry,alarmIndex,alarmVariable=mibBuilder.importSymbols(_B,'alarmEntry',_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxRmon=ModuleIdentity((1,3,6,1,4,1,2636,3,13))
if mibBuilder.loadTexts:jnxRmon.setRevisions(('2005-11-23 00:00','2002-01-10 00:00'))
_JnxRmonAlarmTable_Object=MibTable
jnxRmonAlarmTable=_JnxRmonAlarmTable_Object((1,3,6,1,4,1,2636,3,13,1))
if mibBuilder.loadTexts:jnxRmonAlarmTable.setStatus(_A)
_JnxRmonAlarmEntry_Object=MibTableRow
jnxRmonAlarmEntry=_JnxRmonAlarmEntry_Object((1,3,6,1,4,1,2636,3,13,1,1))
if mibBuilder.loadTexts:jnxRmonAlarmEntry.setStatus(_A)
_JnxRmonAlarmGetFailCnt_Type=Counter32
_JnxRmonAlarmGetFailCnt_Object=MibTableColumn
jnxRmonAlarmGetFailCnt=_JnxRmonAlarmGetFailCnt_Object((1,3,6,1,4,1,2636,3,13,1,1,1),_JnxRmonAlarmGetFailCnt_Type())
jnxRmonAlarmGetFailCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxRmonAlarmGetFailCnt.setStatus(_A)
_JnxRmonAlarmGetFailTime_Type=TimeTicks
_JnxRmonAlarmGetFailTime_Object=MibTableColumn
jnxRmonAlarmGetFailTime=_JnxRmonAlarmGetFailTime_Object((1,3,6,1,4,1,2636,3,13,1,1,2),_JnxRmonAlarmGetFailTime_Type())
jnxRmonAlarmGetFailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxRmonAlarmGetFailTime.setStatus(_A)
class _JnxRmonAlarmGetFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),('noError',2),('noSuchObject',3),('outOfView',4),('noSuchInstance',5),('badReqId',6),('oidMatchErr',7),('oidBindErr',8),('createPktErr',9),('badObjType',10),('processRestarted',11),('lostInstance',12)))
_JnxRmonAlarmGetFailReason_Type.__name__=_F
_JnxRmonAlarmGetFailReason_Object=MibTableColumn
jnxRmonAlarmGetFailReason=_JnxRmonAlarmGetFailReason_Object((1,3,6,1,4,1,2636,3,13,1,1,3),_JnxRmonAlarmGetFailReason_Type())
jnxRmonAlarmGetFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxRmonAlarmGetFailReason.setStatus(_A)
_JnxRmonAlarmGetOkTime_Type=TimeTicks
_JnxRmonAlarmGetOkTime_Object=MibTableColumn
jnxRmonAlarmGetOkTime=_JnxRmonAlarmGetOkTime_Object((1,3,6,1,4,1,2636,3,13,1,1,4),_JnxRmonAlarmGetOkTime_Type())
jnxRmonAlarmGetOkTime.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxRmonAlarmGetOkTime.setStatus(_A)
class _JnxRmonAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('underCreation',2),('active',3),('startup',4),('risingThreshold',5),('fallingThreshold',6),('getFailure',7)))
_JnxRmonAlarmState_Type.__name__=_F
_JnxRmonAlarmState_Object=MibTableColumn
jnxRmonAlarmState=_JnxRmonAlarmState_Object((1,3,6,1,4,1,2636,3,13,1,1,5),_JnxRmonAlarmState_Type())
jnxRmonAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxRmonAlarmState.setStatus(_A)
_JnxRmonTrapPrefix_ObjectIdentity=ObjectIdentity
jnxRmonTrapPrefix=_JnxRmonTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2636,4,3,0))
alarmEntry.registerAugmentions((_G,_H))
jnxRmonAlarmEntry.setIndexNames(*alarmEntry.getIndexNames())
jnxRmonAlarmGetFailure=NotificationType((1,3,6,1,4,1,2636,4,3,0,1))
jnxRmonAlarmGetFailure.setObjects(*((_B,_D),(_B,_E),(_G,_I)))
if mibBuilder.loadTexts:jnxRmonAlarmGetFailure.setStatus(_A)
jnxRmonGetOk=NotificationType((1,3,6,1,4,1,2636,4,3,0,2))
jnxRmonGetOk.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:jnxRmonGetOk.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'jnxRmon':jnxRmon,'jnxRmonAlarmTable':jnxRmonAlarmTable,_H:jnxRmonAlarmEntry,'jnxRmonAlarmGetFailCnt':jnxRmonAlarmGetFailCnt,'jnxRmonAlarmGetFailTime':jnxRmonAlarmGetFailTime,_I:jnxRmonAlarmGetFailReason,'jnxRmonAlarmGetOkTime':jnxRmonAlarmGetOkTime,'jnxRmonAlarmState':jnxRmonAlarmState,'jnxRmonTrapPrefix':jnxRmonTrapPrefix,'jnxRmonAlarmGetFailure':jnxRmonAlarmGetFailure,'jnxRmonGetOk':jnxRmonGetOk})