_c='qtechSecZoneVCMIBGroup'
_b='qtechBockingEntryStatusVC'
_a='qtechBockingTryAccessZoneNameVC'
_Z='qtechBockingCurrentStatusVC'
_Y='qtechZone2ZoneEntryStautsVC'
_X='qtechSecZoneChainEntryStatusVC'
_W='qtechSecZoneViolationBlockTimeoutVC'
_V='qtechSecZoneViolationBlockActionVC'
_U='qtechSecZoneViolationBlockThreshVC'
_T='qtechSecZoneViolationNotifyActionVC'
_S='qtechSecZoneViolationNotifyThreshVC'
_R='qtechSecZoneAclNameVC'
_Q='qtechSecZoneLevelVC'
_P='zoneblock'
_O='globalblock'
_N='qtechBockingIPVC'
_M='qtechBockingContextNameVC'
_L='qtechZone2ZoneAclNameVC'
_K='qtechZoneSecondNameVC'
_J='qtechZoneFirstNameVC'
_I='qtechZone2ZoneContextNameVC'
_H='qtechSecZoneChainNameVC'
_G='qtechSecZoneContextNameVC'
_F='Integer32'
_E='read-create'
_D='read-only'
_C='DisplayString'
_B='current'
_A='QTECH-SECZONE-CONTEXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,=mibBuilder.importSymbols('QTECH-TC','ConfigStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
qtechSecZoneVCMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,68))
if mibBuilder.loadTexts:qtechSecZoneVCMIB.setRevisions(('2009-12-06 00:00',))
_QtechSecZoneVCMIBObjects_ObjectIdentity=ObjectIdentity
qtechSecZoneVCMIBObjects=_QtechSecZoneVCMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,68,1))
_QtechSecZoneChainVCTable_Object=MibTable
qtechSecZoneChainVCTable=_QtechSecZoneChainVCTable_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1))
if mibBuilder.loadTexts:qtechSecZoneChainVCTable.setStatus(_B)
_QtechSecZoneChainVCEntry_Object=MibTableRow
qtechSecZoneChainVCEntry=_QtechSecZoneChainVCEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1))
qtechSecZoneChainVCEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:qtechSecZoneChainVCEntry.setStatus(_B)
class _QtechSecZoneContextNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_QtechSecZoneContextNameVC_Type.__name__=_C
_QtechSecZoneContextNameVC_Object=MibTableColumn
qtechSecZoneContextNameVC=_QtechSecZoneContextNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,1),_QtechSecZoneContextNameVC_Type())
qtechSecZoneContextNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSecZoneContextNameVC.setStatus(_B)
class _QtechSecZoneChainNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSecZoneChainNameVC_Type.__name__=_C
_QtechSecZoneChainNameVC_Object=MibTableColumn
qtechSecZoneChainNameVC=_QtechSecZoneChainNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,2),_QtechSecZoneChainNameVC_Type())
qtechSecZoneChainNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSecZoneChainNameVC.setStatus(_B)
class _QtechSecZoneLevelVC_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechSecZoneLevelVC_Type.__name__=_F
_QtechSecZoneLevelVC_Object=MibTableColumn
qtechSecZoneLevelVC=_QtechSecZoneLevelVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,3),_QtechSecZoneLevelVC_Type())
qtechSecZoneLevelVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneLevelVC.setStatus(_B)
class _QtechSecZoneAclNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSecZoneAclNameVC_Type.__name__=_C
_QtechSecZoneAclNameVC_Object=MibTableColumn
qtechSecZoneAclNameVC=_QtechSecZoneAclNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,4),_QtechSecZoneAclNameVC_Type())
qtechSecZoneAclNameVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneAclNameVC.setStatus(_B)
class _QtechSecZoneViolationNotifyThreshVC_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechSecZoneViolationNotifyThreshVC_Type.__name__=_F
_QtechSecZoneViolationNotifyThreshVC_Object=MibTableColumn
qtechSecZoneViolationNotifyThreshVC=_QtechSecZoneViolationNotifyThreshVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,5),_QtechSecZoneViolationNotifyThreshVC_Type())
qtechSecZoneViolationNotifyThreshVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneViolationNotifyThreshVC.setStatus(_B)
class _QtechSecZoneViolationNotifyActionVC_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('nologtrap',0),('log',1),('trap',2),('logtrap',3)))
_QtechSecZoneViolationNotifyActionVC_Type.__name__=_F
_QtechSecZoneViolationNotifyActionVC_Object=MibTableColumn
qtechSecZoneViolationNotifyActionVC=_QtechSecZoneViolationNotifyActionVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,6),_QtechSecZoneViolationNotifyActionVC_Type())
qtechSecZoneViolationNotifyActionVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneViolationNotifyActionVC.setStatus(_B)
class _QtechSecZoneViolationBlockThreshVC_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechSecZoneViolationBlockThreshVC_Type.__name__=_F
_QtechSecZoneViolationBlockThreshVC_Object=MibTableColumn
qtechSecZoneViolationBlockThreshVC=_QtechSecZoneViolationBlockThreshVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,7),_QtechSecZoneViolationBlockThreshVC_Type())
qtechSecZoneViolationBlockThreshVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneViolationBlockThreshVC.setStatus(_B)
class _QtechSecZoneViolationBlockActionVC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_QtechSecZoneViolationBlockActionVC_Type.__name__=_F
_QtechSecZoneViolationBlockActionVC_Object=MibTableColumn
qtechSecZoneViolationBlockActionVC=_QtechSecZoneViolationBlockActionVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,8),_QtechSecZoneViolationBlockActionVC_Type())
qtechSecZoneViolationBlockActionVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneViolationBlockActionVC.setStatus(_B)
class _QtechSecZoneViolationBlockTimeoutVC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_QtechSecZoneViolationBlockTimeoutVC_Type.__name__=_F
_QtechSecZoneViolationBlockTimeoutVC_Object=MibTableColumn
qtechSecZoneViolationBlockTimeoutVC=_QtechSecZoneViolationBlockTimeoutVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,9),_QtechSecZoneViolationBlockTimeoutVC_Type())
qtechSecZoneViolationBlockTimeoutVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneViolationBlockTimeoutVC.setStatus(_B)
_QtechSecZoneChainEntryStatusVC_Type=RowStatus
_QtechSecZoneChainEntryStatusVC_Object=MibTableColumn
qtechSecZoneChainEntryStatusVC=_QtechSecZoneChainEntryStatusVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,1,1,10),_QtechSecZoneChainEntryStatusVC_Type())
qtechSecZoneChainEntryStatusVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSecZoneChainEntryStatusVC.setStatus(_B)
_QtechSecZone2ZoneVCTable_Object=MibTable
qtechSecZone2ZoneVCTable=_QtechSecZone2ZoneVCTable_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,2))
if mibBuilder.loadTexts:qtechSecZone2ZoneVCTable.setStatus(_B)
_QtechSecZone2ZoneVCEntry_Object=MibTableRow
qtechSecZone2ZoneVCEntry=_QtechSecZone2ZoneVCEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,2,1))
qtechSecZone2ZoneVCEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:qtechSecZone2ZoneVCEntry.setStatus(_B)
class _QtechZone2ZoneContextNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_QtechZone2ZoneContextNameVC_Type.__name__=_C
_QtechZone2ZoneContextNameVC_Object=MibTableColumn
qtechZone2ZoneContextNameVC=_QtechZone2ZoneContextNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,2,1,1),_QtechZone2ZoneContextNameVC_Type())
qtechZone2ZoneContextNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechZone2ZoneContextNameVC.setStatus(_B)
class _QtechZoneFirstNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechZoneFirstNameVC_Type.__name__=_C
_QtechZoneFirstNameVC_Object=MibTableColumn
qtechZoneFirstNameVC=_QtechZoneFirstNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,2,1,2),_QtechZoneFirstNameVC_Type())
qtechZoneFirstNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechZoneFirstNameVC.setStatus(_B)
class _QtechZoneSecondNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechZoneSecondNameVC_Type.__name__=_C
_QtechZoneSecondNameVC_Object=MibTableColumn
qtechZoneSecondNameVC=_QtechZoneSecondNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,2,1,3),_QtechZoneSecondNameVC_Type())
qtechZoneSecondNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechZoneSecondNameVC.setStatus(_B)
class _QtechZone2ZoneAclNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechZone2ZoneAclNameVC_Type.__name__=_C
_QtechZone2ZoneAclNameVC_Object=MibTableColumn
qtechZone2ZoneAclNameVC=_QtechZone2ZoneAclNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,2,1,4),_QtechZone2ZoneAclNameVC_Type())
qtechZone2ZoneAclNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechZone2ZoneAclNameVC.setStatus(_B)
_QtechZone2ZoneEntryStautsVC_Type=RowStatus
_QtechZone2ZoneEntryStautsVC_Object=MibTableColumn
qtechZone2ZoneEntryStautsVC=_QtechZone2ZoneEntryStautsVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,2,1,5),_QtechZone2ZoneEntryStautsVC_Type())
qtechZone2ZoneEntryStautsVC.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechZone2ZoneEntryStautsVC.setStatus(_B)
_QtechSecZoneBlockingVCTable_Object=MibTable
qtechSecZoneBlockingVCTable=_QtechSecZoneBlockingVCTable_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,3))
if mibBuilder.loadTexts:qtechSecZoneBlockingVCTable.setStatus(_B)
_QtechSecZoneBlockingVCEntry_Object=MibTableRow
qtechSecZoneBlockingVCEntry=_QtechSecZoneBlockingVCEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,3,1))
qtechSecZoneBlockingVCEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:qtechSecZoneBlockingVCEntry.setStatus(_B)
class _QtechBockingContextNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_QtechBockingContextNameVC_Type.__name__=_C
_QtechBockingContextNameVC_Object=MibTableColumn
qtechBockingContextNameVC=_QtechBockingContextNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,3,1,1),_QtechBockingContextNameVC_Type())
qtechBockingContextNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBockingContextNameVC.setStatus(_B)
_QtechBockingIPVC_Type=IpAddress
_QtechBockingIPVC_Object=MibTableColumn
qtechBockingIPVC=_QtechBockingIPVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,3,1,2),_QtechBockingIPVC_Type())
qtechBockingIPVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBockingIPVC.setStatus(_B)
class _QtechBockingCurrentStatusVC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_QtechBockingCurrentStatusVC_Type.__name__=_F
_QtechBockingCurrentStatusVC_Object=MibTableColumn
qtechBockingCurrentStatusVC=_QtechBockingCurrentStatusVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,3,1,3),_QtechBockingCurrentStatusVC_Type())
qtechBockingCurrentStatusVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBockingCurrentStatusVC.setStatus(_B)
class _QtechBockingTryAccessZoneNameVC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechBockingTryAccessZoneNameVC_Type.__name__=_C
_QtechBockingTryAccessZoneNameVC_Object=MibTableColumn
qtechBockingTryAccessZoneNameVC=_QtechBockingTryAccessZoneNameVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,3,1,4),_QtechBockingTryAccessZoneNameVC_Type())
qtechBockingTryAccessZoneNameVC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechBockingTryAccessZoneNameVC.setStatus(_B)
_QtechBockingEntryStatusVC_Type=ConfigStatus
_QtechBockingEntryStatusVC_Object=MibTableColumn
qtechBockingEntryStatusVC=_QtechBockingEntryStatusVC_Object((1,3,6,1,4,1,27514,1,1,10,2,68,1,3,1,5),_QtechBockingEntryStatusVC_Type())
qtechBockingEntryStatusVC.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechBockingEntryStatusVC.setStatus(_B)
_QtechSecZoneVCMIBConformance_ObjectIdentity=ObjectIdentity
qtechSecZoneVCMIBConformance=_QtechSecZoneVCMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,68,3))
_QtechSecZoneVCMIBCompliances_ObjectIdentity=ObjectIdentity
qtechSecZoneVCMIBCompliances=_QtechSecZoneVCMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,68,3,1))
_QtechSecZoneVCMIBGroups_ObjectIdentity=ObjectIdentity
qtechSecZoneVCMIBGroups=_QtechSecZoneVCMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,68,3,2))
qtechSecZoneVCMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,68,3,2,1))
qtechSecZoneVCMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_Y),(_A,_M),(_A,_N),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:qtechSecZoneVCMIBGroup.setStatus(_B)
qtechSecZoneVCMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,68,3,1,1))
qtechSecZoneVCMIBCompliance.setObjects((_A,_c))
if mibBuilder.loadTexts:qtechSecZoneVCMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechSecZoneVCMIB':qtechSecZoneVCMIB,'qtechSecZoneVCMIBObjects':qtechSecZoneVCMIBObjects,'qtechSecZoneChainVCTable':qtechSecZoneChainVCTable,'qtechSecZoneChainVCEntry':qtechSecZoneChainVCEntry,_G:qtechSecZoneContextNameVC,_H:qtechSecZoneChainNameVC,_Q:qtechSecZoneLevelVC,_R:qtechSecZoneAclNameVC,_S:qtechSecZoneViolationNotifyThreshVC,_T:qtechSecZoneViolationNotifyActionVC,_U:qtechSecZoneViolationBlockThreshVC,_V:qtechSecZoneViolationBlockActionVC,_W:qtechSecZoneViolationBlockTimeoutVC,_X:qtechSecZoneChainEntryStatusVC,'qtechSecZone2ZoneVCTable':qtechSecZone2ZoneVCTable,'qtechSecZone2ZoneVCEntry':qtechSecZone2ZoneVCEntry,_I:qtechZone2ZoneContextNameVC,_J:qtechZoneFirstNameVC,_K:qtechZoneSecondNameVC,_L:qtechZone2ZoneAclNameVC,_Y:qtechZone2ZoneEntryStautsVC,'qtechSecZoneBlockingVCTable':qtechSecZoneBlockingVCTable,'qtechSecZoneBlockingVCEntry':qtechSecZoneBlockingVCEntry,_M:qtechBockingContextNameVC,_N:qtechBockingIPVC,_Z:qtechBockingCurrentStatusVC,_a:qtechBockingTryAccessZoneNameVC,_b:qtechBockingEntryStatusVC,'qtechSecZoneVCMIBConformance':qtechSecZoneVCMIBConformance,'qtechSecZoneVCMIBCompliances':qtechSecZoneVCMIBCompliances,'qtechSecZoneVCMIBCompliance':qtechSecZoneVCMIBCompliance,'qtechSecZoneVCMIBGroups':qtechSecZoneVCMIBGroups,_c:qtechSecZoneVCMIBGroup})