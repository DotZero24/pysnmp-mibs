_S='snCamUsageOtherType'
_R='snCamUsageOtherProcessor'
_Q='snCamUsageOtherSlot'
_P='snCamUsageSessionType'
_O='snCamUsageSessionProcessor'
_N='snCamUsageSessionSlot'
_M='snCamUsageL2Type'
_L='snCamUsageL2Processor'
_K='snCamUsageL2Slot'
_J='snCamUsageL3Supernet'
_I='snCamUsageL3Type'
_H='snCamUsageL3Processor'
_G='snCamUsageL3Slot'
_F='Integer32'
_E='Entries'
_D='not-accessible'
_C='read-only'
_B='FOUNDRY-SN-CAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
platform,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','platform')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snCamMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,14,1))
if mibBuilder.loadTexts:snCamMIB.setRevisions(('2007-11-19 00:00',))
class Percent(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SnCamObjects_ObjectIdentity=ObjectIdentity
snCamObjects=_SnCamObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,14,1,1))
class _SnCamProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('default',1),('ipv4',2),('ipv4Ipv6',3),('ipv4Ipv62',4),('ipv4Vpls',5),('ipv4Vpn',6),('ipv6',7),('l2Metro',8),('l2Metro2',9),('mplsL3vpn',10),('mplsL3vpn2',11),('mplsVpls',12),('mplsVpls2',13),('mplsVpnVpls',14),('multiService',15),('multiService2',16),('multiService3',17),('multiService4',18),('multiService5',19),('multiService6',20)))
_SnCamProfile_Type.__name__=_F
_SnCamProfile_Object=MibScalar
snCamProfile=_SnCamProfile_Object((1,3,6,1,4,1,1991,1,14,1,1,1),_SnCamProfile_Type())
snCamProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamProfile.setStatus(_A)
_SnCamUsage_ObjectIdentity=ObjectIdentity
snCamUsage=_SnCamUsage_ObjectIdentity((1,3,6,1,4,1,1991,1,14,1,1,2))
_SnCamUsageL3Table_Object=MibTable
snCamUsageL3Table=_SnCamUsageL3Table_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1))
if mibBuilder.loadTexts:snCamUsageL3Table.setStatus(_A)
_SnCamUsageL3Entry_Object=MibTableRow
snCamUsageL3Entry=_SnCamUsageL3Entry_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1))
snCamUsageL3Entry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:snCamUsageL3Entry.setStatus(_A)
_SnCamUsageL3Slot_Type=Unsigned32
_SnCamUsageL3Slot_Object=MibTableColumn
snCamUsageL3Slot=_SnCamUsageL3Slot_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1,1),_SnCamUsageL3Slot_Type())
snCamUsageL3Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageL3Slot.setStatus(_A)
_SnCamUsageL3Processor_Type=Unsigned32
_SnCamUsageL3Processor_Object=MibTableColumn
snCamUsageL3Processor=_SnCamUsageL3Processor_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1,2),_SnCamUsageL3Processor_Type())
snCamUsageL3Processor.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageL3Processor.setStatus(_A)
class _SnCamUsageL3Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('ipv4vpn',3),('ipv6vpn',4)))
_SnCamUsageL3Type_Type.__name__=_F
_SnCamUsageL3Type_Object=MibTableColumn
snCamUsageL3Type=_SnCamUsageL3Type_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1,3),_SnCamUsageL3Type_Type())
snCamUsageL3Type.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageL3Type.setStatus(_A)
_SnCamUsageL3Supernet_Type=Unsigned32
_SnCamUsageL3Supernet_Object=MibTableColumn
snCamUsageL3Supernet=_SnCamUsageL3Supernet_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1,4),_SnCamUsageL3Supernet_Type())
snCamUsageL3Supernet.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageL3Supernet.setStatus(_A)
_SnCamUsageL3Size_Type=Unsigned32
_SnCamUsageL3Size_Object=MibTableColumn
snCamUsageL3Size=_SnCamUsageL3Size_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1,5),_SnCamUsageL3Size_Type())
snCamUsageL3Size.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageL3Size.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageL3Size.setUnits(_E)
_SnCamUsageL3Free_Type=Gauge32
_SnCamUsageL3Free_Object=MibTableColumn
snCamUsageL3Free=_SnCamUsageL3Free_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1,6),_SnCamUsageL3Free_Type())
snCamUsageL3Free.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageL3Free.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageL3Free.setUnits(_E)
_SnCamUsageL3UsedPercent_Type=Percent
_SnCamUsageL3UsedPercent_Object=MibTableColumn
snCamUsageL3UsedPercent=_SnCamUsageL3UsedPercent_Object((1,3,6,1,4,1,1991,1,14,1,1,2,1,1,7),_SnCamUsageL3UsedPercent_Type())
snCamUsageL3UsedPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageL3UsedPercent.setStatus(_A)
_SnCamUsageL2Table_Object=MibTable
snCamUsageL2Table=_SnCamUsageL2Table_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2))
if mibBuilder.loadTexts:snCamUsageL2Table.setStatus(_A)
_SnCamUsageL2Entry_Object=MibTableRow
snCamUsageL2Entry=_SnCamUsageL2Entry_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2,1))
snCamUsageL2Entry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:snCamUsageL2Entry.setStatus(_A)
_SnCamUsageL2Slot_Type=Unsigned32
_SnCamUsageL2Slot_Object=MibTableColumn
snCamUsageL2Slot=_SnCamUsageL2Slot_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2,1,1),_SnCamUsageL2Slot_Type())
snCamUsageL2Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageL2Slot.setStatus(_A)
_SnCamUsageL2Processor_Type=Unsigned32
_SnCamUsageL2Processor_Object=MibTableColumn
snCamUsageL2Processor=_SnCamUsageL2Processor_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2,1,2),_SnCamUsageL2Processor_Type())
snCamUsageL2Processor.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageL2Processor.setStatus(_A)
class _SnCamUsageL2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forwarding',1),('protocol',2),('flooding',3),('total',4)))
_SnCamUsageL2Type_Type.__name__=_F
_SnCamUsageL2Type_Object=MibTableColumn
snCamUsageL2Type=_SnCamUsageL2Type_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2,1,3),_SnCamUsageL2Type_Type())
snCamUsageL2Type.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageL2Type.setStatus(_A)
_SnCamUsageL2Size_Type=Unsigned32
_SnCamUsageL2Size_Object=MibTableColumn
snCamUsageL2Size=_SnCamUsageL2Size_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2,1,4),_SnCamUsageL2Size_Type())
snCamUsageL2Size.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageL2Size.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageL2Size.setUnits(_E)
_SnCamUsageL2Free_Type=Gauge32
_SnCamUsageL2Free_Object=MibTableColumn
snCamUsageL2Free=_SnCamUsageL2Free_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2,1,5),_SnCamUsageL2Free_Type())
snCamUsageL2Free.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageL2Free.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageL2Free.setUnits(_E)
_SnCamUsageL2UsedPercent_Type=Percent
_SnCamUsageL2UsedPercent_Object=MibTableColumn
snCamUsageL2UsedPercent=_SnCamUsageL2UsedPercent_Object((1,3,6,1,4,1,1991,1,14,1,1,2,2,1,6),_SnCamUsageL2UsedPercent_Type())
snCamUsageL2UsedPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageL2UsedPercent.setStatus(_A)
_SnCamUsageSessionTable_Object=MibTable
snCamUsageSessionTable=_SnCamUsageSessionTable_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3))
if mibBuilder.loadTexts:snCamUsageSessionTable.setStatus(_A)
_SnCamUsageSessionEntry_Object=MibTableRow
snCamUsageSessionEntry=_SnCamUsageSessionEntry_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3,1))
snCamUsageSessionEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:snCamUsageSessionEntry.setStatus(_A)
_SnCamUsageSessionSlot_Type=Unsigned32
_SnCamUsageSessionSlot_Object=MibTableColumn
snCamUsageSessionSlot=_SnCamUsageSessionSlot_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3,1,1),_SnCamUsageSessionSlot_Type())
snCamUsageSessionSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageSessionSlot.setStatus(_A)
_SnCamUsageSessionProcessor_Type=Unsigned32
_SnCamUsageSessionProcessor_Object=MibTableColumn
snCamUsageSessionProcessor=_SnCamUsageSessionProcessor_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3,1,2),_SnCamUsageSessionProcessor_Type())
snCamUsageSessionProcessor.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageSessionProcessor.setStatus(_A)
class _SnCamUsageSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('ipv4Multicast',1),('ipv4andMacReceiveAcl',2),('ipv4andMacRuleAcl',3),('ipv4andMacTotal',4),('ipv4andMacOut',5),('ipv6Multicast',6),('ipv6ReceiveAcl',7),('ipv6RuleAcl',8),('ipv6Total',9),('ipv6Out',10),('labelOut',11),('ipv4SrcGuardDenial',12),('ipv4SrcGuardPermit',13),('internalForwardingLookup',14)))
_SnCamUsageSessionType_Type.__name__=_F
_SnCamUsageSessionType_Object=MibTableColumn
snCamUsageSessionType=_SnCamUsageSessionType_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3,1,3),_SnCamUsageSessionType_Type())
snCamUsageSessionType.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageSessionType.setStatus(_A)
_SnCamUsageSessionSize_Type=Unsigned32
_SnCamUsageSessionSize_Object=MibTableColumn
snCamUsageSessionSize=_SnCamUsageSessionSize_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3,1,4),_SnCamUsageSessionSize_Type())
snCamUsageSessionSize.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageSessionSize.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageSessionSize.setUnits(_E)
_SnCamUsageSessionFree_Type=Gauge32
_SnCamUsageSessionFree_Object=MibTableColumn
snCamUsageSessionFree=_SnCamUsageSessionFree_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3,1,5),_SnCamUsageSessionFree_Type())
snCamUsageSessionFree.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageSessionFree.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageSessionFree.setUnits(_E)
_SnCamUsageSessionUsedPercent_Type=Percent
_SnCamUsageSessionUsedPercent_Object=MibTableColumn
snCamUsageSessionUsedPercent=_SnCamUsageSessionUsedPercent_Object((1,3,6,1,4,1,1991,1,14,1,1,2,3,1,6),_SnCamUsageSessionUsedPercent_Type())
snCamUsageSessionUsedPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageSessionUsedPercent.setStatus(_A)
_SnCamUsageOtherTable_Object=MibTable
snCamUsageOtherTable=_SnCamUsageOtherTable_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4))
if mibBuilder.loadTexts:snCamUsageOtherTable.setStatus(_A)
_SnCamUsageOtherEntry_Object=MibTableRow
snCamUsageOtherEntry=_SnCamUsageOtherEntry_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4,1))
snCamUsageOtherEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:snCamUsageOtherEntry.setStatus(_A)
_SnCamUsageOtherSlot_Type=Unsigned32
_SnCamUsageOtherSlot_Object=MibTableColumn
snCamUsageOtherSlot=_SnCamUsageOtherSlot_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4,1,1),_SnCamUsageOtherSlot_Type())
snCamUsageOtherSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageOtherSlot.setStatus(_A)
_SnCamUsageOtherProcessor_Type=Unsigned32
_SnCamUsageOtherProcessor_Object=MibTableColumn
snCamUsageOtherProcessor=_SnCamUsageOtherProcessor_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4,1,2),_SnCamUsageOtherProcessor_Type())
snCamUsageOtherProcessor.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageOtherProcessor.setStatus(_A)
class _SnCamUsageOtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gre',1),('multicastVpls',2)))
_SnCamUsageOtherType_Type.__name__=_F
_SnCamUsageOtherType_Object=MibTableColumn
snCamUsageOtherType=_SnCamUsageOtherType_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4,1,3),_SnCamUsageOtherType_Type())
snCamUsageOtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:snCamUsageOtherType.setStatus(_A)
_SnCamUsageOtherSize_Type=Unsigned32
_SnCamUsageOtherSize_Object=MibTableColumn
snCamUsageOtherSize=_SnCamUsageOtherSize_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4,1,4),_SnCamUsageOtherSize_Type())
snCamUsageOtherSize.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageOtherSize.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageOtherSize.setUnits(_E)
_SnCamUsageOtherFree_Type=Gauge32
_SnCamUsageOtherFree_Object=MibTableColumn
snCamUsageOtherFree=_SnCamUsageOtherFree_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4,1,5),_SnCamUsageOtherFree_Type())
snCamUsageOtherFree.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageOtherFree.setStatus(_A)
if mibBuilder.loadTexts:snCamUsageOtherFree.setUnits(_E)
_SnCamUsageOtherUsedPercent_Type=Percent
_SnCamUsageOtherUsedPercent_Object=MibTableColumn
snCamUsageOtherUsedPercent=_SnCamUsageOtherUsedPercent_Object((1,3,6,1,4,1,1991,1,14,1,1,2,4,1,6),_SnCamUsageOtherUsedPercent_Type())
snCamUsageOtherUsedPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:snCamUsageOtherUsedPercent.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Percent':Percent,'snCamMIB':snCamMIB,'snCamObjects':snCamObjects,'snCamProfile':snCamProfile,'snCamUsage':snCamUsage,'snCamUsageL3Table':snCamUsageL3Table,'snCamUsageL3Entry':snCamUsageL3Entry,_G:snCamUsageL3Slot,_H:snCamUsageL3Processor,_I:snCamUsageL3Type,_J:snCamUsageL3Supernet,'snCamUsageL3Size':snCamUsageL3Size,'snCamUsageL3Free':snCamUsageL3Free,'snCamUsageL3UsedPercent':snCamUsageL3UsedPercent,'snCamUsageL2Table':snCamUsageL2Table,'snCamUsageL2Entry':snCamUsageL2Entry,_K:snCamUsageL2Slot,_L:snCamUsageL2Processor,_M:snCamUsageL2Type,'snCamUsageL2Size':snCamUsageL2Size,'snCamUsageL2Free':snCamUsageL2Free,'snCamUsageL2UsedPercent':snCamUsageL2UsedPercent,'snCamUsageSessionTable':snCamUsageSessionTable,'snCamUsageSessionEntry':snCamUsageSessionEntry,_N:snCamUsageSessionSlot,_O:snCamUsageSessionProcessor,_P:snCamUsageSessionType,'snCamUsageSessionSize':snCamUsageSessionSize,'snCamUsageSessionFree':snCamUsageSessionFree,'snCamUsageSessionUsedPercent':snCamUsageSessionUsedPercent,'snCamUsageOtherTable':snCamUsageOtherTable,'snCamUsageOtherEntry':snCamUsageOtherEntry,_Q:snCamUsageOtherSlot,_R:snCamUsageOtherProcessor,_S:snCamUsageOtherType,'snCamUsageOtherSize':snCamUsageOtherSize,'snCamUsageOtherFree':snCamUsageOtherFree,'snCamUsageOtherUsedPercent':snCamUsageOtherUsedPercent})