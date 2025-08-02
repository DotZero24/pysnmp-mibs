_L='alarmText'
_K='alarmLogInformation'
_J='alarmLogIndex'
_I='NotificationType'
_H='Integer32'
_G='commonPhysAddress'
_F='commonNELogicalID'
_E='OctetString'
_D='NSCRTV-HFCEMS-COMMON-MIB'
_C='NSCRTV-HFCEMS-ALARMS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonNELogicalID,commonPhysAddress=mibBuilder.importSymbols(_D,_F,_G)
alarmsIdent,nscrtvHFCemsTree=mibBuilder.importSymbols('NSCRTV-ROOT','alarmsIdent','nscrtvHFCemsTree')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_AlarmLogNumberOfEntries_Type=Integer32
_AlarmLogNumberOfEntries_Object=MibScalar
alarmLogNumberOfEntries=_AlarmLogNumberOfEntries_Object((1,3,6,1,4,1,17409,1,2,1),_AlarmLogNumberOfEntries_Type())
alarmLogNumberOfEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogNumberOfEntries.setStatus(_A)
_AlarmLogLastIndex_Type=Integer32
_AlarmLogLastIndex_Object=MibScalar
alarmLogLastIndex=_AlarmLogLastIndex_Object((1,3,6,1,4,1,17409,1,2,2),_AlarmLogLastIndex_Type())
alarmLogLastIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogLastIndex.setStatus(_A)
_AlarmLogTable_Object=MibTable
alarmLogTable=_AlarmLogTable_Object((1,3,6,1,4,1,17409,1,2,3))
if mibBuilder.loadTexts:alarmLogTable.setStatus(_A)
_AlarmLogEntry_Object=MibTableRow
alarmLogEntry=_AlarmLogEntry_Object((1,3,6,1,4,1,17409,1,2,3,1))
alarmLogEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:alarmLogEntry.setStatus(_A)
class _AlarmLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_AlarmLogIndex_Type.__name__=_H
_AlarmLogIndex_Object=MibTableColumn
alarmLogIndex=_AlarmLogIndex_Object((1,3,6,1,4,1,17409,1,2,3,1,1),_AlarmLogIndex_Type())
alarmLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogIndex.setStatus(_A)
class _AlarmLogInformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(17,255))
_AlarmLogInformation_Type.__name__=_E
_AlarmLogInformation_Object=MibTableColumn
alarmLogInformation=_AlarmLogInformation_Object((1,3,6,1,4,1,17409,1,2,3,1,2),_AlarmLogInformation_Type())
alarmLogInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLogInformation.setStatus(_A)
_AlarmText_Type=DisplayString
_AlarmText_Object=MibScalar
alarmText=_AlarmText_Object((1,3,6,1,4,1,17409,1,2,4),_AlarmText_Type())
alarmText.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alarmText.setStatus('optional')
hfcAlarmEvent=NotificationType((1,3,6,1,4,1,17409,1,0,1))
hfcAlarmEvent.setObjects(*((_D,_G),(_D,_F),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:hfcAlarmEvent.setStatus('')
mibBuilder.exportSymbols(_C,**{'hfcAlarmEvent':hfcAlarmEvent,'alarmLogNumberOfEntries':alarmLogNumberOfEntries,'alarmLogLastIndex':alarmLogLastIndex,'alarmLogTable':alarmLogTable,'alarmLogEntry':alarmLogEntry,_J:alarmLogIndex,_K:alarmLogInformation,_L:alarmText})