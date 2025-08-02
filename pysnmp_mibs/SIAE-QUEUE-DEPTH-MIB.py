_H='read-write'
_G='qdProfileIndex'
_F='SIAE-QUEUE-DEPTH-MIB'
_E='DisplayString'
_D='Integer32'
_C='AlarmSeverityCode'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_C,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
queueDepth=ModuleIdentity((1,3,6,1,4,1,3373,1103,84))
if mibBuilder.loadTexts:queueDepth.setRevisions(('2014-05-20 00:00',))
class DisplayString1024(TextualConvention,OctetString):status=_A;displayHint='1024a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_QueueDepthMibVersion_Type=Integer32
_QueueDepthMibVersion_Object=MibScalar
queueDepthMibVersion=_QueueDepthMibVersion_Object((1,3,6,1,4,1,3373,1103,84,1),_QueueDepthMibVersion_Type())
queueDepthMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:queueDepthMibVersion.setStatus(_A)
_QdProfileTable_Object=MibTable
qdProfileTable=_QdProfileTable_Object((1,3,6,1,4,1,3373,1103,84,2))
if mibBuilder.loadTexts:qdProfileTable.setStatus(_A)
_QdProfileEntry_Object=MibTableRow
qdProfileEntry=_QdProfileEntry_Object((1,3,6,1,4,1,3373,1103,84,2,1))
qdProfileEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:qdProfileEntry.setStatus(_A)
_QdProfileIndex_Type=Integer32
_QdProfileIndex_Object=MibTableColumn
qdProfileIndex=_QdProfileIndex_Object((1,3,6,1,4,1,3373,1103,84,2,1,1),_QdProfileIndex_Type())
qdProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qdProfileIndex.setStatus(_A)
class _QdProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_QdProfileName_Type.__name__=_E
_QdProfileName_Object=MibTableColumn
qdProfileName=_QdProfileName_Object((1,3,6,1,4,1,3373,1103,84,2,1,2),_QdProfileName_Type())
qdProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:qdProfileName.setStatus(_A)
_QdProfileDescription_Type=DisplayString1024
_QdProfileDescription_Object=MibTableColumn
qdProfileDescription=_QdProfileDescription_Object((1,3,6,1,4,1,3373,1103,84,2,1,3),_QdProfileDescription_Type())
qdProfileDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qdProfileDescription.setStatus(_A)
class _QdProfileSelect_Type(Integer32):defaultValue=1
_QdProfileSelect_Type.__name__=_D
_QdProfileSelect_Object=MibScalar
qdProfileSelect=_QdProfileSelect_Object((1,3,6,1,4,1,3373,1103,84,3),_QdProfileSelect_Type())
qdProfileSelect.setMaxAccess(_H)
if mibBuilder.loadTexts:qdProfileSelect.setStatus(_A)
_QdActualProfile_Type=Integer32
_QdActualProfile_Object=MibScalar
qdActualProfile=_QdActualProfile_Object((1,3,6,1,4,1,3373,1103,84,4),_QdActualProfile_Type())
qdActualProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:qdActualProfile.setStatus(_A)
_QdProfileMismatchAlarm_Type=AlarmStatus
_QdProfileMismatchAlarm_Object=MibScalar
qdProfileMismatchAlarm=_QdProfileMismatchAlarm_Object((1,3,6,1,4,1,3373,1103,84,5),_QdProfileMismatchAlarm_Type())
qdProfileMismatchAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:qdProfileMismatchAlarm.setStatus(_A)
class _QdProfileMismatchAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_QdProfileMismatchAlarmSeverityCode_Type.__name__=_C
_QdProfileMismatchAlarmSeverityCode_Object=MibScalar
qdProfileMismatchAlarmSeverityCode=_QdProfileMismatchAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,84,6),_QdProfileMismatchAlarmSeverityCode_Type())
qdProfileMismatchAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:qdProfileMismatchAlarmSeverityCode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'DisplayString1024':DisplayString1024,'queueDepth':queueDepth,'queueDepthMibVersion':queueDepthMibVersion,'qdProfileTable':qdProfileTable,'qdProfileEntry':qdProfileEntry,_G:qdProfileIndex,'qdProfileName':qdProfileName,'qdProfileDescription':qdProfileDescription,'qdProfileSelect':qdProfileSelect,'qdActualProfile':qdActualProfile,'qdProfileMismatchAlarm':qdProfileMismatchAlarm,'qdProfileMismatchAlarmSeverityCode':qdProfileMismatchAlarmSeverityCode})