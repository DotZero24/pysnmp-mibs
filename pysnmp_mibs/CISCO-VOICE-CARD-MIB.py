_J='ciscoVoiceCardGroup'
_I='cVoiceCardAdminStatus'
_H='cVoiceCardCodecComplexity'
_G='cVoiceCardSlotNumber'
_F='read-write'
_E='cVoiceCardIndex'
_D='Unsigned32'
_C='Integer32'
_B='CISCO-VOICE-CARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVoiceCard=ModuleIdentity((1,3,6,1,4,1,9,9,300576))
if mibBuilder.loadTexts:ciscoVoiceCard.setRevisions(('2002-02-15 00:00',))
_CiscoVoiceCardNotifications_ObjectIdentity=ObjectIdentity
ciscoVoiceCardNotifications=_CiscoVoiceCardNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,300576,0))
_CiscoVoiceCardObjects_ObjectIdentity=ObjectIdentity
ciscoVoiceCardObjects=_CiscoVoiceCardObjects_ObjectIdentity((1,3,6,1,4,1,9,9,300576,1))
_CVoiceCardTable_Object=MibTable
cVoiceCardTable=_CVoiceCardTable_Object((1,3,6,1,4,1,9,9,300576,1,1))
if mibBuilder.loadTexts:cVoiceCardTable.setStatus(_A)
_CVoiceCardEntry_Object=MibTableRow
cVoiceCardEntry=_CVoiceCardEntry_Object((1,3,6,1,4,1,9,9,300576,1,1,1))
cVoiceCardEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cVoiceCardEntry.setStatus(_A)
class _CVoiceCardIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CVoiceCardIndex_Type.__name__=_D
_CVoiceCardIndex_Object=MibTableColumn
cVoiceCardIndex=_CVoiceCardIndex_Object((1,3,6,1,4,1,9,9,300576,1,1,1,1),_CVoiceCardIndex_Type())
cVoiceCardIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cVoiceCardIndex.setStatus(_A)
class _CVoiceCardSlotNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CVoiceCardSlotNumber_Type.__name__=_D
_CVoiceCardSlotNumber_Object=MibTableColumn
cVoiceCardSlotNumber=_CVoiceCardSlotNumber_Object((1,3,6,1,4,1,9,9,300576,1,1,1,2),_CVoiceCardSlotNumber_Type())
cVoiceCardSlotNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:cVoiceCardSlotNumber.setStatus(_A)
class _CVoiceCardCodecComplexity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('hc',2),('mc',4)))
_CVoiceCardCodecComplexity_Type.__name__=_C
_CVoiceCardCodecComplexity_Object=MibTableColumn
cVoiceCardCodecComplexity=_CVoiceCardCodecComplexity_Object((1,3,6,1,4,1,9,9,300576,1,1,1,3),_CVoiceCardCodecComplexity_Type())
cVoiceCardCodecComplexity.setMaxAccess(_F)
if mibBuilder.loadTexts:cVoiceCardCodecComplexity.setStatus(_A)
class _CVoiceCardAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CVoiceCardAdminStatus_Type.__name__=_C
_CVoiceCardAdminStatus_Object=MibTableColumn
cVoiceCardAdminStatus=_CVoiceCardAdminStatus_Object((1,3,6,1,4,1,9,9,300576,1,1,1,4),_CVoiceCardAdminStatus_Type())
cVoiceCardAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cVoiceCardAdminStatus.setStatus(_A)
_CiscoVoiceCardConformance_ObjectIdentity=ObjectIdentity
ciscoVoiceCardConformance=_CiscoVoiceCardConformance_ObjectIdentity((1,3,6,1,4,1,9,9,300576,2))
_CiscoVoiceCardMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVoiceCardMIBCompliances=_CiscoVoiceCardMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,300576,2,1))
_CiscoVoiceCardMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVoiceCardMIBGroups=_CiscoVoiceCardMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,300576,2,2))
ciscoVoiceCardGroup=ObjectGroup((1,3,6,1,4,1,9,9,300576,2,2,1))
ciscoVoiceCardGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ciscoVoiceCardGroup.setStatus(_A)
ciscoVoiceCardMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,300576,2,1,1))
ciscoVoiceCardMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoVoiceCardMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVoiceCard':ciscoVoiceCard,'ciscoVoiceCardNotifications':ciscoVoiceCardNotifications,'ciscoVoiceCardObjects':ciscoVoiceCardObjects,'cVoiceCardTable':cVoiceCardTable,'cVoiceCardEntry':cVoiceCardEntry,_E:cVoiceCardIndex,_G:cVoiceCardSlotNumber,_H:cVoiceCardCodecComplexity,_I:cVoiceCardAdminStatus,'ciscoVoiceCardConformance':ciscoVoiceCardConformance,'ciscoVoiceCardMIBCompliances':ciscoVoiceCardMIBCompliances,'ciscoVoiceCardMIBCompliance':ciscoVoiceCardMIBCompliance,'ciscoVoiceCardMIBGroups':ciscoVoiceCardMIBGroups,_J:ciscoVoiceCardGroup})