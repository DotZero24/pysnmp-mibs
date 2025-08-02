_L='fsVrrpOperEntry'
_K='fsVrrpOperTrackGroupIfIndex'
_J='not-accessible'
_I='disabled'
_H='enabled'
_G='fsVrrpOperTrackGroupIndex'
_F='read-create'
_E='Unsigned32'
_D='ARICENT-VRRP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
vrrpOperEntry,=mibBuilder.importSymbols('VRRP-MIB','vrrpOperEntry')
fsvrrp=ModuleIdentity((1,3,6,1,4,1,2076,153))
if mibBuilder.loadTexts:fsvrrp.setRevisions(('2013-11-18 00:00','2011-09-12 00:00','2011-08-30 00:00','2011-03-11 00:00','2006-08-03 00:00','2006-04-06 00:00'))
_FsVrrpSystem_ObjectIdentity=ObjectIdentity
fsVrrpSystem=_FsVrrpSystem_ObjectIdentity((1,3,6,1,4,1,2076,153,1))
class _FsVrrpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsVrrpStatus_Type.__name__=_B
_FsVrrpStatus_Object=MibScalar
fsVrrpStatus=_FsVrrpStatus_Object((1,3,6,1,4,1,2076,153,1,1),_FsVrrpStatus_Type())
fsVrrpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpStatus.setStatus(_A)
_FsVrrpMaxOperEntries_Type=Integer32
_FsVrrpMaxOperEntries_Object=MibScalar
fsVrrpMaxOperEntries=_FsVrrpMaxOperEntries_Object((1,3,6,1,4,1,2076,153,1,2),_FsVrrpMaxOperEntries_Type())
fsVrrpMaxOperEntries.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsVrrpMaxOperEntries.setStatus(_A)
_FsVrrpOperTable_Object=MibTable
fsVrrpOperTable=_FsVrrpOperTable_Object((1,3,6,1,4,1,2076,153,1,3))
if mibBuilder.loadTexts:fsVrrpOperTable.setStatus(_A)
_FsVrrpOperEntry_Object=MibTableRow
fsVrrpOperEntry=_FsVrrpOperEntry_Object((1,3,6,1,4,1,2076,153,1,3,1))
if mibBuilder.loadTexts:fsVrrpOperEntry.setStatus(_A)
class _FsVrrpAdminPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_FsVrrpAdminPriority_Type.__name__=_B
_FsVrrpAdminPriority_Object=MibTableColumn
fsVrrpAdminPriority=_FsVrrpAdminPriority_Object((1,3,6,1,4,1,2076,153,1,3,1,1),_FsVrrpAdminPriority_Type())
fsVrrpAdminPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpAdminPriority.setStatus(_A)
class _FsVrrpOperAdvertisementIntervalInMsec_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,255000))
_FsVrrpOperAdvertisementIntervalInMsec_Type.__name__=_B
_FsVrrpOperAdvertisementIntervalInMsec_Object=MibTableColumn
fsVrrpOperAdvertisementIntervalInMsec=_FsVrrpOperAdvertisementIntervalInMsec_Object((1,3,6,1,4,1,2076,153,1,3,1,2),_FsVrrpOperAdvertisementIntervalInMsec_Type())
fsVrrpOperAdvertisementIntervalInMsec.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVrrpOperAdvertisementIntervalInMsec.setStatus(_A)
if mibBuilder.loadTexts:fsVrrpOperAdvertisementIntervalInMsec.setUnits('milli seconds')
class _FsVrrpOperTrackGroupId_Type(Unsigned32):defaultValue=0
_FsVrrpOperTrackGroupId_Type.__name__=_E
_FsVrrpOperTrackGroupId_Object=MibTableColumn
fsVrrpOperTrackGroupId=_FsVrrpOperTrackGroupId_Object((1,3,6,1,4,1,2076,153,1,3,1,3),_FsVrrpOperTrackGroupId_Type())
fsVrrpOperTrackGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpOperTrackGroupId.setStatus(_A)
class _FsVrrpOperDecrementPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_FsVrrpOperDecrementPriority_Type.__name__=_E
_FsVrrpOperDecrementPriority_Object=MibTableColumn
fsVrrpOperDecrementPriority=_FsVrrpOperDecrementPriority_Object((1,3,6,1,4,1,2076,153,1,3,1,4),_FsVrrpOperDecrementPriority_Type())
fsVrrpOperDecrementPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpOperDecrementPriority.setStatus(_A)
class _FsVrrpAuthDeprecate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsVrrpAuthDeprecate_Type.__name__=_B
_FsVrrpAuthDeprecate_Object=MibScalar
fsVrrpAuthDeprecate=_FsVrrpAuthDeprecate_Object((1,3,6,1,4,1,2076,153,1,4),_FsVrrpAuthDeprecate_Type())
fsVrrpAuthDeprecate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpAuthDeprecate.setStatus(_A)
class _FsVrrpTraceOption_Type(Integer32):defaultValue=0
_FsVrrpTraceOption_Type.__name__=_B
_FsVrrpTraceOption_Object=MibScalar
fsVrrpTraceOption=_FsVrrpTraceOption_Object((1,3,6,1,4,1,2076,153,1,5),_FsVrrpTraceOption_Type())
fsVrrpTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpTraceOption.setStatus(_A)
_FsVrrpOperTrackGroupTable_Object=MibTable
fsVrrpOperTrackGroupTable=_FsVrrpOperTrackGroupTable_Object((1,3,6,1,4,1,2076,153,1,6))
if mibBuilder.loadTexts:fsVrrpOperTrackGroupTable.setStatus(_A)
_FsVrrpOperTrackGroupEntry_Object=MibTableRow
fsVrrpOperTrackGroupEntry=_FsVrrpOperTrackGroupEntry_Object((1,3,6,1,4,1,2076,153,1,6,1))
fsVrrpOperTrackGroupEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsVrrpOperTrackGroupEntry.setStatus(_A)
_FsVrrpOperTrackGroupIndex_Type=Unsigned32
_FsVrrpOperTrackGroupIndex_Object=MibTableColumn
fsVrrpOperTrackGroupIndex=_FsVrrpOperTrackGroupIndex_Object((1,3,6,1,4,1,2076,153,1,6,1,1),_FsVrrpOperTrackGroupIndex_Type())
fsVrrpOperTrackGroupIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsVrrpOperTrackGroupIndex.setStatus(_A)
class _FsVrrpOperTrackedGroupTrackedLinks_Type(Unsigned32):defaultValue=0
_FsVrrpOperTrackedGroupTrackedLinks_Type.__name__=_E
_FsVrrpOperTrackedGroupTrackedLinks_Object=MibTableColumn
fsVrrpOperTrackedGroupTrackedLinks=_FsVrrpOperTrackedGroupTrackedLinks_Object((1,3,6,1,4,1,2076,153,1,6,1,2),_FsVrrpOperTrackedGroupTrackedLinks_Type())
fsVrrpOperTrackedGroupTrackedLinks.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVrrpOperTrackedGroupTrackedLinks.setStatus(_A)
_FsVrrpOperTrackRowStatus_Type=RowStatus
_FsVrrpOperTrackRowStatus_Object=MibTableColumn
fsVrrpOperTrackRowStatus=_FsVrrpOperTrackRowStatus_Object((1,3,6,1,4,1,2076,153,1,6,1,3),_FsVrrpOperTrackRowStatus_Type())
fsVrrpOperTrackRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVrrpOperTrackRowStatus.setStatus(_A)
_FsVrrpOperTrackGroupIfTable_Object=MibTable
fsVrrpOperTrackGroupIfTable=_FsVrrpOperTrackGroupIfTable_Object((1,3,6,1,4,1,2076,153,1,7))
if mibBuilder.loadTexts:fsVrrpOperTrackGroupIfTable.setStatus(_A)
_FsVrrpOperTrackGroupIfEntry_Object=MibTableRow
fsVrrpOperTrackGroupIfEntry=_FsVrrpOperTrackGroupIfEntry_Object((1,3,6,1,4,1,2076,153,1,7,1))
fsVrrpOperTrackGroupIfEntry.setIndexNames((0,_D,_G),(0,_D,_K))
if mibBuilder.loadTexts:fsVrrpOperTrackGroupIfEntry.setStatus(_A)
_FsVrrpOperTrackGroupIfIndex_Type=InterfaceIndexOrZero
_FsVrrpOperTrackGroupIfIndex_Object=MibTableColumn
fsVrrpOperTrackGroupIfIndex=_FsVrrpOperTrackGroupIfIndex_Object((1,3,6,1,4,1,2076,153,1,7,1,1),_FsVrrpOperTrackGroupIfIndex_Type())
fsVrrpOperTrackGroupIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsVrrpOperTrackGroupIfIndex.setStatus(_A)
_FsVrrpOperTrackGroupIfRowStatus_Type=RowStatus
_FsVrrpOperTrackGroupIfRowStatus_Object=MibTableColumn
fsVrrpOperTrackGroupIfRowStatus=_FsVrrpOperTrackGroupIfRowStatus_Object((1,3,6,1,4,1,2076,153,1,7,1,2),_FsVrrpOperTrackGroupIfRowStatus_Type())
fsVrrpOperTrackGroupIfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVrrpOperTrackGroupIfRowStatus.setStatus(_A)
vrrpOperEntry.registerAugmentions((_D,_L))
fsVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'fsvrrp':fsvrrp,'fsVrrpSystem':fsVrrpSystem,'fsVrrpStatus':fsVrrpStatus,'fsVrrpMaxOperEntries':fsVrrpMaxOperEntries,'fsVrrpOperTable':fsVrrpOperTable,_L:fsVrrpOperEntry,'fsVrrpAdminPriority':fsVrrpAdminPriority,'fsVrrpOperAdvertisementIntervalInMsec':fsVrrpOperAdvertisementIntervalInMsec,'fsVrrpOperTrackGroupId':fsVrrpOperTrackGroupId,'fsVrrpOperDecrementPriority':fsVrrpOperDecrementPriority,'fsVrrpAuthDeprecate':fsVrrpAuthDeprecate,'fsVrrpTraceOption':fsVrrpTraceOption,'fsVrrpOperTrackGroupTable':fsVrrpOperTrackGroupTable,'fsVrrpOperTrackGroupEntry':fsVrrpOperTrackGroupEntry,_G:fsVrrpOperTrackGroupIndex,'fsVrrpOperTrackedGroupTrackedLinks':fsVrrpOperTrackedGroupTrackedLinks,'fsVrrpOperTrackRowStatus':fsVrrpOperTrackRowStatus,'fsVrrpOperTrackGroupIfTable':fsVrrpOperTrackGroupIfTable,'fsVrrpOperTrackGroupIfEntry':fsVrrpOperTrackGroupIfEntry,_K:fsVrrpOperTrackGroupIfIndex,'fsVrrpOperTrackGroupIfRowStatus':fsVrrpOperTrackGroupIfRowStatus})