_K='OctetString'
_J='atFiberMonThreshold'
_I='atFiberMonReading'
_H='atFiberMonChannel'
_G='atFiberMonIfindex'
_F='atFiberMonIfname'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='AT-FIBER-MONITORING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SYSINFO-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atFiberMon=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,27))
if mibBuilder.loadTexts:atFiberMon.setRevisions(('2020-06-16 00:00','2015-09-08 00:00'))
_AtFiberMonNotifications_ObjectIdentity=ObjectIdentity
atFiberMonNotifications=_AtFiberMonNotifications_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,27,0))
_AtFiberMonTrapVariable_ObjectIdentity=ObjectIdentity
atFiberMonTrapVariable=_AtFiberMonTrapVariable_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,27,1))
class _AtFiberMonReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtFiberMonReading_Type.__name__=_C
_AtFiberMonReading_Object=MibScalar
atFiberMonReading=_AtFiberMonReading_Object((1,3,6,1,4,1,207,8,4,4,3,27,1,1),_AtFiberMonReading_Type())
atFiberMonReading.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:atFiberMonReading.setStatus(_A)
_AtFiberMonConfigTable_Object=MibTable
atFiberMonConfigTable=_AtFiberMonConfigTable_Object((1,3,6,1,4,1,207,8,4,4,3,27,2))
if mibBuilder.loadTexts:atFiberMonConfigTable.setStatus(_A)
_AtFiberMonConfigEntry_Object=MibTableRow
atFiberMonConfigEntry=_AtFiberMonConfigEntry_Object((1,3,6,1,4,1,207,8,4,4,3,27,2,1))
atFiberMonConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:atFiberMonConfigEntry.setStatus(_A)
class _AtFiberMonIfname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AtFiberMonIfname_Type.__name__=_K
_AtFiberMonIfname_Object=MibTableColumn
atFiberMonIfname=_AtFiberMonIfname_Object((1,3,6,1,4,1,207,8,4,4,3,27,2,1,1),_AtFiberMonIfname_Type())
atFiberMonIfname.setMaxAccess(_E)
if mibBuilder.loadTexts:atFiberMonIfname.setStatus(_A)
class _AtFiberMonEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AtFiberMonEnable_Type.__name__=_C
_AtFiberMonEnable_Object=MibTableColumn
atFiberMonEnable=_AtFiberMonEnable_Object((1,3,6,1,4,1,207,8,4,4,3,27,2,1,2),_AtFiberMonEnable_Type())
atFiberMonEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:atFiberMonEnable.setStatus(_A)
class _AtFiberMonInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,60))
_AtFiberMonInterval_Type.__name__=_C
_AtFiberMonInterval_Object=MibTableColumn
atFiberMonInterval=_AtFiberMonInterval_Object((1,3,6,1,4,1,207,8,4,4,3,27,2,1,3),_AtFiberMonInterval_Type())
atFiberMonInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:atFiberMonInterval.setStatus(_A)
_AtFiberMonSensitivity_Type=OctetString
_AtFiberMonSensitivity_Object=MibTableColumn
atFiberMonSensitivity=_AtFiberMonSensitivity_Object((1,3,6,1,4,1,207,8,4,4,3,27,2,1,4),_AtFiberMonSensitivity_Type())
atFiberMonSensitivity.setMaxAccess(_E)
if mibBuilder.loadTexts:atFiberMonSensitivity.setStatus(_A)
_AtFiberMonBaseline_Type=OctetString
_AtFiberMonBaseline_Object=MibTableColumn
atFiberMonBaseline=_AtFiberMonBaseline_Object((1,3,6,1,4,1,207,8,4,4,3,27,2,1,5),_AtFiberMonBaseline_Type())
atFiberMonBaseline.setMaxAccess(_E)
if mibBuilder.loadTexts:atFiberMonBaseline.setStatus(_A)
class _AtFiberMonAlarmAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('logOnly',1),('sendTrap',2),('shutdown',3),('sendtrapAndShutdown',4)))
_AtFiberMonAlarmAction_Type.__name__=_C
_AtFiberMonAlarmAction_Object=MibTableColumn
atFiberMonAlarmAction=_AtFiberMonAlarmAction_Object((1,3,6,1,4,1,207,8,4,4,3,27,2,1,6),_AtFiberMonAlarmAction_Type())
atFiberMonAlarmAction.setMaxAccess(_E)
if mibBuilder.loadTexts:atFiberMonAlarmAction.setStatus(_A)
_AtFiberMonStateTable_Object=MibTable
atFiberMonStateTable=_AtFiberMonStateTable_Object((1,3,6,1,4,1,207,8,4,4,3,27,3))
if mibBuilder.loadTexts:atFiberMonStateTable.setStatus(_A)
_AtFiberMonStateEntry_Object=MibTableRow
atFiberMonStateEntry=_AtFiberMonStateEntry_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1))
atFiberMonStateEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:atFiberMonStateEntry.setStatus(_A)
class _AtFiberMonIfindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AtFiberMonIfindex_Type.__name__=_C
_AtFiberMonIfindex_Object=MibTableColumn
atFiberMonIfindex=_AtFiberMonIfindex_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,1),_AtFiberMonIfindex_Type())
atFiberMonIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonIfindex.setStatus(_A)
class _AtFiberMonChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AtFiberMonChannel_Type.__name__=_C
_AtFiberMonChannel_Object=MibTableColumn
atFiberMonChannel=_AtFiberMonChannel_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,2),_AtFiberMonChannel_Type())
atFiberMonChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonChannel.setStatus(_A)
_AtFiberMonlIfDescription_Type=DisplayString
_AtFiberMonlIfDescription_Object=MibTableColumn
atFiberMonlIfDescription=_AtFiberMonlIfDescription_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,3),_AtFiberMonlIfDescription_Type())
atFiberMonlIfDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonlIfDescription.setStatus(_A)
class _AtFiberMonActualBaseline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtFiberMonActualBaseline_Type.__name__=_C
_AtFiberMonActualBaseline_Object=MibTableColumn
atFiberMonActualBaseline=_AtFiberMonActualBaseline_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,4),_AtFiberMonActualBaseline_Type())
atFiberMonActualBaseline.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonActualBaseline.setStatus(_A)
class _AtFiberMonThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtFiberMonThreshold_Type.__name__=_C
_AtFiberMonThreshold_Object=MibTableColumn
atFiberMonThreshold=_AtFiberMonThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,5),_AtFiberMonThreshold_Type())
atFiberMonThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonThreshold.setStatus(_A)
_AtFiberMonReadingHistory_Type=DisplayString
_AtFiberMonReadingHistory_Object=MibTableColumn
atFiberMonReadingHistory=_AtFiberMonReadingHistory_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,6),_AtFiberMonReadingHistory_Type())
atFiberMonReadingHistory.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonReadingHistory.setStatus(_A)
class _AtFiberMonMinReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtFiberMonMinReading_Type.__name__=_C
_AtFiberMonMinReading_Object=MibTableColumn
atFiberMonMinReading=_AtFiberMonMinReading_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,7),_AtFiberMonMinReading_Type())
atFiberMonMinReading.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonMinReading.setStatus(_A)
class _AtFiberMonMaxReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtFiberMonMaxReading_Type.__name__=_C
_AtFiberMonMaxReading_Object=MibTableColumn
atFiberMonMaxReading=_AtFiberMonMaxReading_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,8),_AtFiberMonMaxReading_Type())
atFiberMonMaxReading.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonMaxReading.setStatus(_A)
class _AtFiberMonLastReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_AtFiberMonLastReading_Type.__name__=_C
_AtFiberMonLastReading_Object=MibTableColumn
atFiberMonLastReading=_AtFiberMonLastReading_Object((1,3,6,1,4,1,207,8,4,4,3,27,3,1,9),_AtFiberMonLastReading_Type())
atFiberMonLastReading.setMaxAccess(_D)
if mibBuilder.loadTexts:atFiberMonLastReading.setStatus(_A)
atFiberMonAlarmSetNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,3,27,0,1))
atFiberMonAlarmSetNotify.setObjects(*((_B,_G),(_B,_H),(_B,_F),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:atFiberMonAlarmSetNotify.setStatus(_A)
atFiberMonAlarmClearedNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,3,27,0,2))
atFiberMonAlarmClearedNotify.setObjects(*((_B,_G),(_B,_H),(_B,_F),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:atFiberMonAlarmClearedNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atFiberMon':atFiberMon,'atFiberMonNotifications':atFiberMonNotifications,'atFiberMonAlarmSetNotify':atFiberMonAlarmSetNotify,'atFiberMonAlarmClearedNotify':atFiberMonAlarmClearedNotify,'atFiberMonTrapVariable':atFiberMonTrapVariable,_I:atFiberMonReading,'atFiberMonConfigTable':atFiberMonConfigTable,'atFiberMonConfigEntry':atFiberMonConfigEntry,_F:atFiberMonIfname,'atFiberMonEnable':atFiberMonEnable,'atFiberMonInterval':atFiberMonInterval,'atFiberMonSensitivity':atFiberMonSensitivity,'atFiberMonBaseline':atFiberMonBaseline,'atFiberMonAlarmAction':atFiberMonAlarmAction,'atFiberMonStateTable':atFiberMonStateTable,'atFiberMonStateEntry':atFiberMonStateEntry,_G:atFiberMonIfindex,_H:atFiberMonChannel,'atFiberMonlIfDescription':atFiberMonlIfDescription,'atFiberMonActualBaseline':atFiberMonActualBaseline,_J:atFiberMonThreshold,'atFiberMonReadingHistory':atFiberMonReadingHistory,'atFiberMonMinReading':atFiberMonMinReading,'atFiberMonMaxReading':atFiberMonMaxReading,'atFiberMonLastReading':atFiberMonLastReading})