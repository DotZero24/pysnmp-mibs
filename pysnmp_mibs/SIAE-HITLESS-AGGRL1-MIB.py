_H='hlLinkStatusEntry'
_G='hlLinkSettingsEntry'
_F='hlAggrL1Entry'
_E='read-write'
_D='read-only'
_C='SIAE-HITLESS-AGGRL1-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aggrL1Entry,=mibBuilder.importSymbols('SIAE-AGGRL1-MANAGEMENT-MIB','aggrL1Entry')
linkSettingsEntry,linkStatusEntry=mibBuilder.importSymbols('SIAE-RADIO-SYSTEM-MIB','linkSettingsEntry','linkStatusEntry')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hitlessAggregationL1=ModuleIdentity((1,3,6,1,4,1,3373,1103,98))
if mibBuilder.loadTexts:hitlessAggregationL1.setRevisions(('2016-12-20 00:00','2016-02-29 00:00'))
_HlAggrL1MibVersion_Type=Integer32
_HlAggrL1MibVersion_Object=MibScalar
hlAggrL1MibVersion=_HlAggrL1MibVersion_Object((1,3,6,1,4,1,3373,1103,98,1),_HlAggrL1MibVersion_Type())
hlAggrL1MibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hlAggrL1MibVersion.setStatus(_A)
_HlAggrL1Table_Object=MibTable
hlAggrL1Table=_HlAggrL1Table_Object((1,3,6,1,4,1,3373,1103,98,2))
if mibBuilder.loadTexts:hlAggrL1Table.setStatus(_A)
_HlAggrL1Entry_Object=MibTableRow
hlAggrL1Entry=_HlAggrL1Entry_Object((1,3,6,1,4,1,3373,1103,98,2,1))
if mibBuilder.loadTexts:hlAggrL1Entry.setStatus(_A)
class _HlAggrL1Mode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hlAggrL1Auto',1),('hlAggrL1Manual',2)))
_HlAggrL1Mode_Type.__name__=_B
_HlAggrL1Mode_Object=MibTableColumn
hlAggrL1Mode=_HlAggrL1Mode_Object((1,3,6,1,4,1,3373,1103,98,2,1,1),_HlAggrL1Mode_Type())
hlAggrL1Mode.setMaxAccess(_E)
if mibBuilder.loadTexts:hlAggrL1Mode.setStatus(_A)
class _HlAggrL1Behaviour_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hlAggrL1AllSurvive',1),('hlAggrL1OneSurvive',2),('hlAggrL1NoneSurvive',3)))
_HlAggrL1Behaviour_Type.__name__=_B
_HlAggrL1Behaviour_Object=MibTableColumn
hlAggrL1Behaviour=_HlAggrL1Behaviour_Object((1,3,6,1,4,1,3373,1103,98,2,1,2),_HlAggrL1Behaviour_Type())
hlAggrL1Behaviour.setMaxAccess(_E)
if mibBuilder.loadTexts:hlAggrL1Behaviour.setStatus(_A)
_HlLinkSettingsTable_Object=MibTable
hlLinkSettingsTable=_HlLinkSettingsTable_Object((1,3,6,1,4,1,3373,1103,98,3))
if mibBuilder.loadTexts:hlLinkSettingsTable.setStatus(_A)
_HlLinkSettingsEntry_Object=MibTableRow
hlLinkSettingsEntry=_HlLinkSettingsEntry_Object((1,3,6,1,4,1,3373,1103,98,3,1))
if mibBuilder.loadTexts:hlLinkSettingsEntry.setStatus(_A)
_LinkHitlessProfile_Type=Integer32
_LinkHitlessProfile_Object=MibTableColumn
linkHitlessProfile=_LinkHitlessProfile_Object((1,3,6,1,4,1,3373,1103,98,3,1,1),_LinkHitlessProfile_Type())
linkHitlessProfile.setMaxAccess('read-create')
if mibBuilder.loadTexts:linkHitlessProfile.setStatus(_A)
_HlLinkStatusTable_Object=MibTable
hlLinkStatusTable=_HlLinkStatusTable_Object((1,3,6,1,4,1,3373,1103,98,4))
if mibBuilder.loadTexts:hlLinkStatusTable.setStatus(_A)
_HlLinkStatusEntry_Object=MibTableRow
hlLinkStatusEntry=_HlLinkStatusEntry_Object((1,3,6,1,4,1,3373,1103,98,4,1))
if mibBuilder.loadTexts:hlLinkStatusEntry.setStatus(_A)
class _LinkHitlessZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('goodZone',1),('hitlessZone',2),('badZone',3),('disqualified',4)))
_LinkHitlessZone_Type.__name__=_B
_LinkHitlessZone_Object=MibTableColumn
linkHitlessZone=_LinkHitlessZone_Object((1,3,6,1,4,1,3373,1103,98,4,1,1),_LinkHitlessZone_Type())
linkHitlessZone.setMaxAccess(_D)
if mibBuilder.loadTexts:linkHitlessZone.setStatus(_A)
aggrL1Entry.registerAugmentions((_C,_F))
hlAggrL1Entry.setIndexNames(*aggrL1Entry.getIndexNames())
linkSettingsEntry.registerAugmentions((_C,_G))
hlLinkSettingsEntry.setIndexNames(*linkSettingsEntry.getIndexNames())
linkStatusEntry.registerAugmentions((_C,_H))
hlLinkStatusEntry.setIndexNames(*linkStatusEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'hitlessAggregationL1':hitlessAggregationL1,'hlAggrL1MibVersion':hlAggrL1MibVersion,'hlAggrL1Table':hlAggrL1Table,_F:hlAggrL1Entry,'hlAggrL1Mode':hlAggrL1Mode,'hlAggrL1Behaviour':hlAggrL1Behaviour,'hlLinkSettingsTable':hlLinkSettingsTable,_G:hlLinkSettingsEntry,'linkHitlessProfile':linkHitlessProfile,'hlLinkStatusTable':hlLinkStatusTable,_H:hlLinkStatusEntry,'linkHitlessZone':linkHitlessZone})