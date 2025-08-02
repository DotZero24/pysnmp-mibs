_N='bsLldpXdot3RemPowerEntry'
_M='bsLldpXdot3LocPowerEntry'
_L='critical'
_K='reserved'
_J='type1pd'
_I='type1pse'
_H='type2pd'
_G='type2pse'
_F='BAY-STACK-LLDP-EXT-DOT3-MIB'
_E='tenth of watt'
_D='unknown'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lldpXdot3LocPowerEntry,lldpXdot3RemPowerEntry=mibBuilder.importSymbols('LLDP-EXT-DOT3-MIB','lldpXdot3LocPowerEntry','lldpXdot3RemPowerEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackLldpXDot3Mib=ModuleIdentity((1,3,6,1,4,1,45,5,47))
if mibBuilder.loadTexts:bayStackLldpXDot3Mib.setRevisions(('2014-10-22 00:00',))
_BsLldpXDot3Notifications_ObjectIdentity=ObjectIdentity
bsLldpXDot3Notifications=_BsLldpXDot3Notifications_ObjectIdentity((1,3,6,1,4,1,45,5,47,0))
_BsLldpXDot3Objects_ObjectIdentity=ObjectIdentity
bsLldpXDot3Objects=_BsLldpXDot3Objects_ObjectIdentity((1,3,6,1,4,1,45,5,47,1))
_BsLldpXdot3Config_ObjectIdentity=ObjectIdentity
bsLldpXdot3Config=_BsLldpXdot3Config_ObjectIdentity((1,3,6,1,4,1,45,5,47,1,1))
_BsLldpXdot3LocalData_ObjectIdentity=ObjectIdentity
bsLldpXdot3LocalData=_BsLldpXdot3LocalData_ObjectIdentity((1,3,6,1,4,1,45,5,47,1,2))
_BsLldpXdot3LocPowerTable_Object=MibTable
bsLldpXdot3LocPowerTable=_BsLldpXdot3LocPowerTable_Object((1,3,6,1,4,1,45,5,47,1,2,1))
if mibBuilder.loadTexts:bsLldpXdot3LocPowerTable.setStatus(_A)
_BsLldpXdot3LocPowerEntry_Object=MibTableRow
bsLldpXdot3LocPowerEntry=_BsLldpXdot3LocPowerEntry_Object((1,3,6,1,4,1,45,5,47,1,2,1,1))
if mibBuilder.loadTexts:bsLldpXdot3LocPowerEntry.setStatus(_A)
class _BsLldpXdot3LocPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_BsLldpXdot3LocPowerType_Type.__name__=_B
_BsLldpXdot3LocPowerType_Object=MibTableColumn
bsLldpXdot3LocPowerType=_BsLldpXdot3LocPowerType_Object((1,3,6,1,4,1,45,5,47,1,2,1,1,1),_BsLldpXdot3LocPowerType_Type())
bsLldpXdot3LocPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3LocPowerType.setStatus(_A)
class _BsLldpXdot3LocPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('primaryPs',2),('backupPs',3),(_K,4)))
_BsLldpXdot3LocPowerSource_Type.__name__=_B
_BsLldpXdot3LocPowerSource_Object=MibTableColumn
bsLldpXdot3LocPowerSource=_BsLldpXdot3LocPowerSource_Object((1,3,6,1,4,1,45,5,47,1,2,1,1,2),_BsLldpXdot3LocPowerSource_Type())
bsLldpXdot3LocPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3LocPowerSource.setStatus(_A)
class _BsLldpXdot3LocPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_L,2),('high',3),('low',4)))
_BsLldpXdot3LocPowerPriority_Type.__name__=_B
_BsLldpXdot3LocPowerPriority_Object=MibTableColumn
bsLldpXdot3LocPowerPriority=_BsLldpXdot3LocPowerPriority_Object((1,3,6,1,4,1,45,5,47,1,2,1,1,3),_BsLldpXdot3LocPowerPriority_Type())
bsLldpXdot3LocPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3LocPowerPriority.setStatus(_A)
class _BsLldpXdot3LocPDRequestedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BsLldpXdot3LocPDRequestedPowerValue_Type.__name__=_B
_BsLldpXdot3LocPDRequestedPowerValue_Object=MibTableColumn
bsLldpXdot3LocPDRequestedPowerValue=_BsLldpXdot3LocPDRequestedPowerValue_Object((1,3,6,1,4,1,45,5,47,1,2,1,1,4),_BsLldpXdot3LocPDRequestedPowerValue_Type())
bsLldpXdot3LocPDRequestedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3LocPDRequestedPowerValue.setStatus(_A)
if mibBuilder.loadTexts:bsLldpXdot3LocPDRequestedPowerValue.setUnits(_E)
class _BsLldpXdot3LocPSEAllocatedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BsLldpXdot3LocPSEAllocatedPowerValue_Type.__name__=_B
_BsLldpXdot3LocPSEAllocatedPowerValue_Object=MibTableColumn
bsLldpXdot3LocPSEAllocatedPowerValue=_BsLldpXdot3LocPSEAllocatedPowerValue_Object((1,3,6,1,4,1,45,5,47,1,2,1,1,5),_BsLldpXdot3LocPSEAllocatedPowerValue_Type())
bsLldpXdot3LocPSEAllocatedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3LocPSEAllocatedPowerValue.setStatus(_A)
if mibBuilder.loadTexts:bsLldpXdot3LocPSEAllocatedPowerValue.setUnits(_E)
_BsLldpXdot3RemoteData_ObjectIdentity=ObjectIdentity
bsLldpXdot3RemoteData=_BsLldpXdot3RemoteData_ObjectIdentity((1,3,6,1,4,1,45,5,47,1,3))
_BsLldpXdot3RemPowerTable_Object=MibTable
bsLldpXdot3RemPowerTable=_BsLldpXdot3RemPowerTable_Object((1,3,6,1,4,1,45,5,47,1,3,1))
if mibBuilder.loadTexts:bsLldpXdot3RemPowerTable.setStatus(_A)
_BsLldpXdot3RemPowerEntry_Object=MibTableRow
bsLldpXdot3RemPowerEntry=_BsLldpXdot3RemPowerEntry_Object((1,3,6,1,4,1,45,5,47,1,3,1,1))
if mibBuilder.loadTexts:bsLldpXdot3RemPowerEntry.setStatus(_A)
class _BsLldpXdot3RemPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_BsLldpXdot3RemPowerType_Type.__name__=_B
_BsLldpXdot3RemPowerType_Object=MibTableColumn
bsLldpXdot3RemPowerType=_BsLldpXdot3RemPowerType_Object((1,3,6,1,4,1,45,5,47,1,3,1,1,1),_BsLldpXdot3RemPowerType_Type())
bsLldpXdot3RemPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3RemPowerType.setStatus(_A)
class _BsLldpXdot3RemPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('pse',2),(_K,3),('pseAndLocal',4)))
_BsLldpXdot3RemPowerSource_Type.__name__=_B
_BsLldpXdot3RemPowerSource_Object=MibTableColumn
bsLldpXdot3RemPowerSource=_BsLldpXdot3RemPowerSource_Object((1,3,6,1,4,1,45,5,47,1,3,1,1,2),_BsLldpXdot3RemPowerSource_Type())
bsLldpXdot3RemPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3RemPowerSource.setStatus(_A)
class _BsLldpXdot3RemPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),(_L,2),('high',3),('low',4)))
_BsLldpXdot3RemPowerPriority_Type.__name__=_B
_BsLldpXdot3RemPowerPriority_Object=MibTableColumn
bsLldpXdot3RemPowerPriority=_BsLldpXdot3RemPowerPriority_Object((1,3,6,1,4,1,45,5,47,1,3,1,1,3),_BsLldpXdot3RemPowerPriority_Type())
bsLldpXdot3RemPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3RemPowerPriority.setStatus(_A)
class _BsLldpXdot3RemPDRequestedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BsLldpXdot3RemPDRequestedPowerValue_Type.__name__=_B
_BsLldpXdot3RemPDRequestedPowerValue_Object=MibTableColumn
bsLldpXdot3RemPDRequestedPowerValue=_BsLldpXdot3RemPDRequestedPowerValue_Object((1,3,6,1,4,1,45,5,47,1,3,1,1,4),_BsLldpXdot3RemPDRequestedPowerValue_Type())
bsLldpXdot3RemPDRequestedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3RemPDRequestedPowerValue.setStatus(_A)
if mibBuilder.loadTexts:bsLldpXdot3RemPDRequestedPowerValue.setUnits(_E)
class _BsLldpXdot3RemPSEAllocatedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BsLldpXdot3RemPSEAllocatedPowerValue_Type.__name__=_B
_BsLldpXdot3RemPSEAllocatedPowerValue_Object=MibTableColumn
bsLldpXdot3RemPSEAllocatedPowerValue=_BsLldpXdot3RemPSEAllocatedPowerValue_Object((1,3,6,1,4,1,45,5,47,1,3,1,1,5),_BsLldpXdot3RemPSEAllocatedPowerValue_Type())
bsLldpXdot3RemPSEAllocatedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXdot3RemPSEAllocatedPowerValue.setStatus(_A)
if mibBuilder.loadTexts:bsLldpXdot3RemPSEAllocatedPowerValue.setUnits(_E)
lldpXdot3LocPowerEntry.registerAugmentions((_F,_M))
bsLldpXdot3LocPowerEntry.setIndexNames(*lldpXdot3LocPowerEntry.getIndexNames())
lldpXdot3RemPowerEntry.registerAugmentions((_F,_N))
bsLldpXdot3RemPowerEntry.setIndexNames(*lldpXdot3RemPowerEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'bayStackLldpXDot3Mib':bayStackLldpXDot3Mib,'bsLldpXDot3Notifications':bsLldpXDot3Notifications,'bsLldpXDot3Objects':bsLldpXDot3Objects,'bsLldpXdot3Config':bsLldpXdot3Config,'bsLldpXdot3LocalData':bsLldpXdot3LocalData,'bsLldpXdot3LocPowerTable':bsLldpXdot3LocPowerTable,_M:bsLldpXdot3LocPowerEntry,'bsLldpXdot3LocPowerType':bsLldpXdot3LocPowerType,'bsLldpXdot3LocPowerSource':bsLldpXdot3LocPowerSource,'bsLldpXdot3LocPowerPriority':bsLldpXdot3LocPowerPriority,'bsLldpXdot3LocPDRequestedPowerValue':bsLldpXdot3LocPDRequestedPowerValue,'bsLldpXdot3LocPSEAllocatedPowerValue':bsLldpXdot3LocPSEAllocatedPowerValue,'bsLldpXdot3RemoteData':bsLldpXdot3RemoteData,'bsLldpXdot3RemPowerTable':bsLldpXdot3RemPowerTable,_N:bsLldpXdot3RemPowerEntry,'bsLldpXdot3RemPowerType':bsLldpXdot3RemPowerType,'bsLldpXdot3RemPowerSource':bsLldpXdot3RemPowerSource,'bsLldpXdot3RemPowerPriority':bsLldpXdot3RemPowerPriority,'bsLldpXdot3RemPDRequestedPowerValue':bsLldpXdot3RemPDRequestedPowerValue,'bsLldpXdot3RemPSEAllocatedPowerValue':bsLldpXdot3RemPSEAllocatedPowerValue})